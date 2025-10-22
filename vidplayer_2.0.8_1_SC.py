
import io
import json
import math
import sys
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import webbrowser
import requests
import time
from pathlib import Path
from typing import Optional, List

# Optional external libraries
try:
    import pygame
except Exception as e:
    raise SystemExit("Missing dependency 'pygame'. Install with: pip install pygame") from e

try:
    from mutagen import File as MutagenFile  # type: ignore
except Exception:
    MutagenFile = None  # type: ignore

try:
    from PIL import Image, ImageTk  # type: ignore
except Exception:
    Image = None  # type: ignore
    ImageTk = None  # type: ignore

# Optional Discord presence
try:
    from pypresence import Presence  # type: ignore
except Exception:
    Presence = None  # type: ignore

from tkinter import filedialog, messagebox
from tkinter import ttk

# App constants
APP_NAME = "VidPlayer"
VERSION = "v2.0.8.1"
DISCORD_APP_ID = "1415851081753296997"
HERE = Path(__file__).parent
CONFIG_FILE = HERE / "config.json"
RECENTS_FILE = HERE / "recents.json"
ARTMAP_FILE = HERE / "artmap.json"  # persist mapping audio -> external artwork

# Add new settings keys: always_on_top, discord_rpc_enabled
DEFAULT_CONFIG = {
    "theme": "system",
    "auto_load_last_playlist": False,
    "default_volume": 50.0,
    "last_volume": 50.0,
    "resume_last": False,
    "last_playlist_path": None,
    "last_index": 0,
    "last_position": 0.0,
    "auto_play_next": True,
    "always_on_top": False,
    "discord_rpc_enabled": False
}


def format_time(seconds: float) -> str:
    if math.isinf(seconds) or seconds < 0:
        seconds = 0
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"


def ensure_json_files():
    """Ensure basic JSON files exist (config, recents, artmap)."""
    if not CONFIG_FILE.exists():
        try:
            CONFIG_FILE.write_text(json.dumps(DEFAULT_CONFIG, indent=2), encoding="utf-8")
        except Exception:
            pass
    if not RECENTS_FILE.exists():
        try:
            RECENTS_FILE.write_text(json.dumps([], indent=2), encoding="utf-8")
        except Exception:
            pass
    if not ARTMAP_FILE.exists():
        try:
            ARTMAP_FILE.write_text(json.dumps({}, indent=2), encoding="utf-8")
        except Exception:
            pass


def load_json(path: Path, default):
    try:
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        pass
    return default


def save_json(path: Path, data):
    try:
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except Exception:
        pass


def get_album_art_bytes(path: Path) -> Optional[bytes]:
    """
    Extract embedded album art bytes via Mutagen (if available).
    Returns None if not available.
    """
    if MutagenFile is None:
        return None
    try:
        f = MutagenFile(str(path))
        if not f:
            return None
        tags = getattr(f, "tags", None)
        if tags:
            for k in tags.keys():
                if str(k).upper().startswith("APIC"):
                    return tags[k].data
            if "covr" in tags:
                covr = tags["covr"]
                if isinstance(covr, list) and covr:
                    return bytes(covr[0])
        # Some formats expose .pictures
        if hasattr(f, "pictures") and getattr(f, "pictures"):
            pic = f.pictures[0]
            return pic.data
    except Exception:
        return None
    return None


def ensure_license_file() -> Path:
    lic_path = HERE / "LICENSE.txt"
    if not lic_path.exists():
        default_text = """vidplayer License Agreement
============================

Copyright (c) 2025 [sonic Fan Tech/sonic Fan Games]

1. Grant of Use
---------------
This software, vidplayer, is provided free of charge for personal, non-commercial use.

2. Restrictions
---------------
- Redistribution of this software in any form is not permitted.
- Modification, reverse engineering, or resale of this software is strictly prohibited.
- This software may not be bundled with or distributed alongside any other products without prior written permission.

3. Ownership
------------
All rights, title, and interest in and to vidplayer remain with the author.

4. Disclaimer of Warranty
-------------------------
This software is provided "as-is," without any warranties, express or implied, including but not limited to fitness for a particular purpose or merchantability.  
The author shall not be held liable for any damages arising from the use of this software.

5. Acceptance
-------------
By installing or using vidplayer, you agree to the terms of this license agreement.
"""
        try:
            lic_path.write_text(default_text, encoding="utf-8")
        except Exception:
            pass
    return lic_path


def ensure_features_file() -> Path:
    features_path = HERE / "FEATURES.txt"
    if not features_path.exists():
        default_text = """Features / Update Log
=======================

Program Re-Wright in Python 3.12+ - v2.0.0
Player UI Re-Done Again, Added Light/Dark Mode Feature, Added recent Files Feature - v2.0.1
Added Art-Work Show Support, Added a Settings Window, Changed how the volume Slider works [Broke it], Added Playlist Support - v2.0.2
Added Auto-Play Next File in Playlist Feature [Build NOT Working, Not Released to the Public] - v2.0.3
Fixed Auto-play Next file in Playlist Feature, Added more settings to the Settings Window - v2.0.4
Added a progress Loading Window that show only when you open More then 10 Files - v2.0.5
Added the New About Window - v2.0.6
updated the License Agreement, made the License and Features / Update Log Tab Load Text from a File, NO CODE NEEDED FOR SAID TEXT, Added a Auto-Check for updates Feature at start up, Added a Check for updates button to the About Menu - v2.0.6.1
Added Discord RPC, Changed the default volume to 50.0 - v2.0.7
Added a Discord Rich Presence toggle in Settings (enables/disables RPC at runtime). When enabled the app holds a single Presence connection and PlaylistWindow uses it, Added an Always on Top setting in Settings, Added Full Screen entry to the Tools menu. Full-screen opens a fullscreen Toplevel that shows the artwork prominently and supports: [Escape to exit fullscreen, Clicking the artwork toggles play/pause, A small label shows filename and a close button], All new settings are saved to CONFIG_FILE and loaded at startup - v2.0.8
added External artwork persistence across restarts [saved to artmap.json], added Prev / Next buttons in the fullscreen overlay, Overlay auto-hide after a few seconds of inactivity and reappear on mouse move, Also keeps the "choose external artwork when embedded missing" flow, but now it persists the choice immediately. - v2.0.8.1
"""
        try:
            features_path.write_text(default_text, encoding="utf-8")
        except Exception:
            pass
    return features_path


def check_for_update(current_version: str, parent=None, manual=False):
    """
    Query GitHub latest release. If manual=True and no update found, show info box.
    """
    url = "https://api.github.com/repos/sonicFanTech/vidplayer/releases/latest"
    try:
        resp = requests.get(url, timeout=6)
        if resp.status_code == 200:
            data = resp.json()
            latest = data.get("tag_name", "").strip()
            assets = data.get("assets", [])
            download_url = assets[0].get("browser_download_url") if assets else None
            if latest and latest != current_version:
                show_update_window(current_version, latest, download_url, parent)
            elif manual:
                messagebox.showinfo("Check for Updates", "No new updates were found.")
        else:
            if manual:
                messagebox.showerror("Update Check Failed", f"HTTP {resp.status_code}")
    except Exception as e:
        if manual:
            messagebox.showerror("Update Check Failed", f"Could not check for updates:\n{e}")
        else:
            print("Update check failed:", e)


def show_update_window(current_version: str, latest_version: str, download_url: Optional[str], parent=None):
    win = tk.Toplevel(parent)
    win.title("Update Available")
    win.geometry("420x260")
    win.resizable(False, False)

    ttk.Label(win, text=f"A new version of {APP_NAME} is available!", font=("Segoe UI", 12, "bold")).pack(pady=10)
    ttk.Label(win, text=f"Current version: {current_version}\nLatest version: {latest_version}", justify="center").pack(pady=5)

    progress = ttk.Progressbar(win, orient="horizontal", mode="determinate", length=300)
    progress.pack(pady=10)
    status_lbl = ttk.Label(win, text="")
    status_lbl.pack()

    def open_releases():
        webbrowser.open("https://github.com/sonicFanTech/vidplayer/releases")
        win.destroy()

    def download_direct():
        if not download_url:
            messagebox.showwarning("No Asset", "No downloadable file was found in this release.")
            return
        save_path = filedialog.asksaveasfilename(title="Save New Version", defaultextension=".exe",
                                                 filetypes=[("Executable", "*.exe"), ("All Files", "*.*")])
        if not save_path:
            return
        try:
            r = requests.get(download_url, stream=True, timeout=10)
            total = int(r.headers.get("content-length", 0))
            written = 0
            with open(save_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if not chunk:
                        continue
                    f.write(chunk)
                    written += len(chunk)
                    if total > 0:
                        progress["value"] = written * 100 / total
                        status_lbl.config(text=f"Downloading... {written//1024} KB / {total//1024} KB")
                        win.update_idletasks()
            status_lbl.config(text="Download complete!")
            messagebox.showinfo("Update Downloaded", f"New version downloaded to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Download Failed", f"Error: {e}")

    ttk.Button(win, text="Download via Program", command=download_direct).pack(pady=4)
    ttk.Button(win, text="Open Releases Page", command=open_releases).pack(pady=4)
    ttk.Button(win, text="Skip for Now", command=win.destroy).pack(pady=4)

    win.transient(parent)
    win.grab_set()


class AboutWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title(f"About {APP_NAME}")
        self.geometry("480x420")
        self.resizable(False, False)

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True, padx=10, pady=10)

        about_frame = ttk.Frame(nb, padding=10)
        ttk.Label(about_frame, text=f"{APP_NAME} {VERSION}\nA simple audio player with playlist, album art,\nsettings, and recent files support.", justify="center").pack(expand=True)
        nb.add(about_frame, text="About")

        credits_frame = ttk.Frame(nb, padding=10)
        ttk.Label(credits_frame, text="Credits:\n\nPython, Tkinter, Pygame\nMutagen, Pillow\npypresence (Discord RPC)\n\nDeveloped by Sonic Fan Tech", justify="left").pack(anchor="w")
        nb.add(credits_frame, text="Credits")

        license_frame = ttk.Frame(nb, padding=10)
        lic_path = ensure_license_file()
        try:
            license_text = lic_path.read_text(encoding="utf-8")
        except Exception:
            license_text = "License file not available."
        st_license = scrolledtext.ScrolledText(license_frame, wrap="word", height=18, width=70)
        st_license.insert("1.0", license_text)
        st_license.config(state="disabled")
        st_license.pack(fill="both", expand=True, padx=5, pady=5)
        nb.add(license_frame, text="License")

        features_frame = ttk.Frame(nb, padding=10)
        features_path = ensure_features_file()
        try:
            features_text = features_path.read_text(encoding="utf-8")
        except Exception:
            features_text = "Features / Update Log file not available."
        st_features = scrolledtext.ScrolledText(features_frame, wrap="word", height=18, width=70)
        st_features.insert("1.0", features_text)
        st_features.config(state="disabled")
        st_features.pack(fill="both", expand=True, padx=5, pady=5)
        nb.add(features_frame, text="Features / Log")

        btnrow = ttk.Frame(self, padding=(8, 6))
        btnrow.pack(fill="x")
        ttk.Button(btnrow, text="Check for Updates Now", command=lambda: check_for_update(VERSION, self, manual=True)).pack(side="left", padx=6)
        ttk.Button(btnrow, text="Open Releases Page", command=lambda: webbrowser.open("https://github.com/sonicFanTech/vidplayer/releases")).pack(side="left", padx=6)

        self.transient(master)
        self.grab_set()


class PlaylistWindow(tk.Toplevel):
    def __init__(self, master: "VidPlayerApp"):
        super().__init__(master)
        self.master = master
        self.title("Playlist")
        self.geometry("520x360")
        self.protocol("WM_DELETE_WINDOW", self.withdraw)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Use the app-level RPC if present
        self.rpc = getattr(master, "rpc", None)

        frame = ttk.Frame(self, padding=8)
        frame.grid(sticky="nsew")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.listbox = tk.Listbox(frame, activestyle="none", selectmode="browse")
        self.listbox.grid(row=0, column=0, sticky="nsew")
        sb = ttk.Scrollbar(frame, orient="vertical", command=self.listbox.yview)
        sb.grid(row=0, column=1, sticky="ns")
        self.listbox.config(yscrollcommand=sb.set)

        btnrow = ttk.Frame(frame)
        btnrow.grid(row=1, column=0, columnspan=2, pady=(8, 0), sticky="ew")
        ttk.Button(btnrow, text="Add Files…", command=self.add_files).pack(side="left", padx=4)
        ttk.Button(btnrow, text="Remove Selected", command=self.remove_selected).pack(side="left", padx=4)
        ttk.Button(btnrow, text="Play Selected", command=self.play_selected).pack(side="left", padx=4)
        ttk.Button(btnrow, text="Previous", command=self.master.play_previous).pack(side="left", padx=4)
        ttk.Button(btnrow, text="Next", command=self.master.play_next).pack(side="left", padx=4)
        ttk.Button(btnrow, text="Save Playlist…", command=self.save_playlist).pack(side="left", padx=4)
        ttk.Button(btnrow, text="Load Playlist…", command=self.load_playlist).pack(side="left", padx=4)

        self.listbox.bind("<Double-Button-1>", lambda e: self.play_selected())
        self.refresh_from_master()

    def refresh_from_master(self):
        self.listbox.delete(0, "end")
        for p in self.master.playlist:
            self.listbox.insert("end", Path(p).name)
        idx = self.master.current_index
        if 0 <= idx < len(self.master.playlist):
            self.listbox.selection_clear(0, "end")
            self.listbox.selection_set(idx)
            self.listbox.see(idx)

    def add_files(self):
        filetypes = [("Audio Files", "*.mp3 *.wav *.ogg *.flac *.m4a"), ("All Files", "*.*")]
        paths = filedialog.askopenfilenames(title="Add audio files", filetypes=filetypes)
        if not paths:
            return
        for p in paths:
            self.master.add_to_playlist(Path(p))
        self.refresh_from_master()

    def remove_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        self.master.remove_from_playlist(idx)
        self.refresh_from_master()

    def play_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            idx = self.listbox.index("active") if self.listbox.size() else 0
        else:
            idx = sel[0]
        self.master.play_index(idx)
        self.refresh_from_master()

    def save_playlist(self):
        path = filedialog.asksaveasfilename(title="Save Playlist", defaultextension=".vpl",
                                            filetypes=[("VidPlayer Playlist", "*.vpl"), ("JSON", "*.json")])
        if not path:
            return
        try:
            self.master.save_playlist(Path(path))
            messagebox.showinfo("Saved", f"Playlist saved to {path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_playlist(self):
        path = filedialog.askopenfilename(title="Load Playlist",
                                          filetypes=[("VidPlayer Playlist", "*.vpl"), ("JSON", "*.json"), ("All Files", "*.*")])
        if not path:
            return
        try:
            self.master.load_playlist(Path(path))
            self.refresh_from_master()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_presence_idle(self):
        if not self.rpc:
            return
        try:
            self.rpc.update(state="No file loaded", details=f"{APP_NAME} {VERSION}",
                            large_image="vidplayer_logo", large_text=APP_NAME)
        except Exception as e:
            print("RPC error (idle):", e)

    def update_presence_playing(self, filename: str, duration: float):
        if not self.rpc:
            return
        try:
            start_time = int(time.time())
            self.rpc.update(state=f"Playing: {filename}", details=f"{APP_NAME} {VERSION}",
                            large_image="vidplayer_logo", large_text=filename,
                            start=start_time, end=(start_time + int(duration) if duration and duration > 0 else None))
        except Exception as e:
            print("RPC error (playing):", e)


class SettingsWindow(tk.Toplevel):
    def __init__(self, master: "VidPlayerApp"):
        super().__init__(master)
        self.master = master
        self.title("Settings")
        self.geometry("420x340")
        self.resizable(False, False)

        frame = ttk.Frame(self, padding=12)
        frame.pack(fill="both", expand=True)

        # Theme
        ttk.Label(frame, text="Theme:").grid(row=0, column=0, sticky="w", pady=4)
        self.theme_var = tk.StringVar(value=self.master.config_data.get("theme", "system"))
        ttk.Radiobutton(frame, text="Light", variable=self.theme_var, value="light").grid(row=0, column=1, sticky="w")
        ttk.Radiobutton(frame, text="Dark", variable=self.theme_var, value="dark").grid(row=0, column=2, sticky="w")
        ttk.Radiobutton(frame, text="System Default", variable=self.theme_var, value="system").grid(row=0, column=3, sticky="w")

        # Auto-load last playlist
        self.auto_load_var = tk.BooleanVar(value=self.master.config_data.get("auto_load_last_playlist", False))
        ttk.Checkbutton(frame, text="Auto-load last playlist on startup", variable=self.auto_load_var).grid(row=1, column=0, columnspan=4, sticky="w", pady=6)

        # Resume last track & position on startup
        self.resume_var = tk.BooleanVar(value=self.master.config_data.get("resume_last", False))
        ttk.Checkbutton(frame, text="Resume last track & position on startup", variable=self.resume_var).grid(row=2, column=0, columnspan=4, sticky="w", pady=6)

        # Autoplay next
        self.autoplay_var = tk.BooleanVar(value=self.master.config_data.get("auto_play_next", True))
        ttk.Checkbutton(frame, text="Autoplay next file in playlist", variable=self.autoplay_var).grid(row=3, column=0, columnspan=3, sticky="w", pady=6)

        # Discord RPC toggle
        self.discord_var = tk.BooleanVar(value=self.master.config_data.get("discord_rpc_enabled", False))
        ttk.Checkbutton(frame, text="Enable Discord Rich Presence", variable=self.discord_var).grid(row=4, column=0, columnspan=3, sticky="w", pady=6)

        # Always on top
        self.always_on_top_var = tk.BooleanVar(value=self.master.config_data.get("always_on_top", False))
        ttk.Checkbutton(frame, text="Always on top", variable=self.always_on_top_var).grid(row=5, column=0, columnspan=3, sticky="w", pady=6)

        # Clear recent files
        ttk.Button(frame, text="Clear Recent Files", command=self.confirm_clear_recent).grid(row=6, column=0, columnspan=2, pady=12)

        btnrow = ttk.Frame(frame)
        btnrow.grid(row=8, column=0, columnspan=4, pady=16)
        ttk.Button(btnrow, text="Save & Close", command=self.on_save).pack(side="left", padx=6)
        ttk.Button(btnrow, text="Cancel", command=self.destroy).pack(side="left", padx=6)

    def confirm_clear_recent(self):
        if messagebox.askyesno("Confirm", "Clear all recent files?"):
            if messagebox.askyesno("Confirm Again", "Really clear recent files? This cannot be undone."):
                save_json(RECENTS_FILE, [])
                self.master.recents = []
                self.master.rebuild_recent_menu()

    def on_save(self):
        # Write settings back to config_data and save
        self.master.config_data["theme"] = self.theme_var.get()
        self.master.config_data["auto_load_last_playlist"] = bool(self.auto_load_var.get())
        self.master.config_data["resume_last"] = bool(self.resume_var.get())
        self.master.config_data["auto_play_next"] = bool(self.autoplay_var.get())
        self.master.config_data["discord_rpc_enabled"] = bool(self.discord_var.get())
        self.master.config_data["always_on_top"] = bool(self.always_on_top_var.get())
        save_json(CONFIG_FILE, self.master.config_data)

        # Apply changes immediately
        self.master.apply_settings_from_config()

        # Manage RPC according to setting
        if self.master.config_data.get("discord_rpc_enabled", False):
            self.master.enable_rpc()
        else:
            self.master.disable_rpc()

        # Apply always-on-top immediately
        self.master.attributes("-topmost", bool(self.master.config_data.get("always_on_top", False)))

        self.destroy()


class VidPlayerApp(tk.Tk):
    POLL_MS = 150
    MAX_RECENTS = 10
    OVERLAY_AUTOHIDE_SEC = 3.0

    def __init__(self):
        super().__init__()
        self.title(f"{APP_NAME} {VERSION}")
        self.geometry("640x360")
        self.minsize(520, 320)
        self.protocol("WM_DELETE_WINDOW", self._quit)

        ensure_json_files()

        # Load config & recents early
        self.config_data = load_json(CONFIG_FILE, DEFAULT_CONFIG.copy())
        for k, v in DEFAULT_CONFIG.items():
            if k not in self.config_data:
                self.config_data[k] = v

        self.recents: List[str] = load_json(RECENTS_FILE, [])

        # State
        self.audio_path: Optional[Path] = None
        self.audio_len_s: float = 0.0
        self.user_is_scrubbing: bool = False
        self._last_seek_value: float = 0.0
        self._paused: bool = False
        self._last_open_dir: Path = Path.home()
        self.playlist: List[str] = []
        self.current_index: int = -1

        # RPC handle (app-level). If enabled in config we will attempt to create it.
        self.rpc = None

        # map audio file -> external artwork path (persisted via ARTMAP_FILE)
        self.external_art_map = load_json(ARTMAP_FILE, {})

        # Init mixer BEFORE any set_volume calls
        self._init_mixer()

        # UI style + var
        self.style = ttk.Style(self)

        # volume var (use config)
        self.vol_var = tk.DoubleVar(value=float(self.config_data.get("last_volume", self.config_data.get("default_volume", 50.0))))

        # Build UI
        self.playlist_window: Optional[PlaylistWindow] = None
        self._build_menu()
        self._build_widgets()
        self._bind_shortcuts()

        # Apply settings (safe now)
        self.apply_settings_from_config(initial=True)

        # Apply always_on_top
        self.attributes("-topmost", bool(self.config_data.get("always_on_top", False)))

        # Possibly enable RPC if configured
        if self.config_data.get("discord_rpc_enabled", False):
            self.enable_rpc()

        # Auto-load last playlist if set
        if self.config_data.get("auto_load_last_playlist") and self.config_data.get("last_playlist_path"):
            last = self.config_data.get("last_playlist_path")
            if last and Path(last).exists():
                self.load_playlist(Path(last))

        # Resume last position if configured
        if self.config_data.get("resume_last"):
            try:
                self.current_index = int(self.config_data.get("last_index", 0))
                self._last_seek_value = float(self.config_data.get("last_position", 0.0))
            except Exception:
                self.current_index, self._last_seek_value = -1, 0.0

        # Start poll loop
        self.after(self.POLL_MS, self._poll)

        # Run background update check after a moment (non-manual)
        self.after(1000, lambda: check_for_update(VERSION, self, manual=False))

    # Mixer init
    def _init_mixer(self) -> None:
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
        except Exception as e:
            messagebox.showerror("Audio Error", f"Could not initialize audio device:\n{e}")

    # RPC management (app-level)
    def enable_rpc(self):
        if not Presence:
            messagebox.showwarning("Discord RPC", "pypresence not installed; cannot enable Discord Rich Presence.")
            self.config_data["discord_rpc_enabled"] = False
            save_json(CONFIG_FILE, self.config_data)
            return
        if self.rpc:
            return
        try:
            self.rpc = Presence(DISCORD_APP_ID)
            self.rpc.connect()
            # set idle if nothing playing
            try:
                self.rpc.update(details="Idle", state=f"{APP_NAME} {VERSION}", large_image="vidplayer_logo", large_text=APP_NAME)
            except Exception:
                pass
            # if playlist window exists, let it reference the same rpc
            if self.playlist_window:
                self.playlist_window.rpc = self.rpc
        except Exception as e:
            print("Discord RPC not connected:", e)
            self.rpc = None
            messagebox.showwarning("Discord RPC", f"Could not connect to Discord RPC:\n{e}")
            self.config_data["discord_rpc_enabled"] = False
            save_json(CONFIG_FILE, self.config_data)

    def disable_rpc(self):
        if not self.rpc:
            return
        try:
            try:
                self.rpc.clear()
            except Exception:
                pass
            try:
                self.rpc.close()
            except Exception:
                pass
        finally:
            self.rpc = None
            if self.playlist_window:
                self.playlist_window.rpc = None

    # Menu
    def _build_menu(self) -> None:
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Files…", command=self.open_files, accelerator="Ctrl+O")
        file_menu.add_command(label="Open Single File…", command=self.open_single_file)
        self.recent_menu = tk.Menu(file_menu, tearoff=0)
        self.rebuild_recent_menu()
        file_menu.add_cascade(label="Recent Files", menu=self.recent_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Save Playlist…", command=self.save_playlist, accelerator="Ctrl+S")
        file_menu.add_command(label="Load Playlist…", command=self.load_playlist)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit, accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=file_menu)

        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Playlist", command=self.open_playlist_window, accelerator="Ctrl+L")
        menubar.add_cascade(label="View", menu=view_menu)

        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Settings", command=self.open_settings, accelerator="Ctrl+T")
        tools_menu.add_command(label="Full Screen Artwork", command=self.open_fullscreen_art)
        menubar.add_cascade(label="Tools", menu=tools_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self._show_about)
        help_menu.add_command(label="Check for Updates…", command=lambda: check_for_update(VERSION, self, manual=True))
        menubar.add_cascade(label="Help", menu=help_menu)

    def rebuild_recent_menu(self):
        self.recent_menu.delete(0, "end")
        if not self.recents:
            self.recent_menu.add_command(label="(None)", state="disabled")
        else:
            for p in self.recents[: self.MAX_RECENTS]:
                pp = Path(p)
                self.recent_menu.add_command(label=pp.name, command=lambda p=pp: self.open_recent(p))

    # Widgets
    def _build_widgets(self) -> None:
        top = ttk.Frame(self, padding=8)
        top.pack(fill="x")

        art_frame = ttk.Frame(top)
        art_frame.pack(side="left", padx=(4, 8))
        self.art_canvas = tk.Label(art_frame)
        self.art_canvas.pack()

        file_row = ttk.Frame(top)
        file_row.pack(fill="x", expand=True, side="left")
        self.lbl_title = ttk.Label(file_row, text=APP_NAME, font=("Segoe UI", 11, "bold"))
        self.lbl_title.pack(anchor="w")
        self.lbl_file = ttk.Label(file_row, text="No file loaded", font=("Segoe UI", 9))
        self.lbl_file.pack(anchor="w")

        controls = ttk.Frame(self, padding=8)
        controls.pack(fill="x")
        self.btn_play = ttk.Button(controls, text="Play", command=self.play_current, state="disabled")
        self.btn_play.pack(side="left")
        self.btn_pause = ttk.Button(controls, text="Pause", command=self.toggle_pause, state="disabled")
        self.btn_pause.pack(side="left", padx=6)
        self.btn_stop = ttk.Button(controls, text="Stop", command=self.stop_audio, state="disabled")
        self.btn_stop.pack(side="left", padx=6)
        ttk.Button(controls, text="Prev", command=self.play_previous).pack(side="left", padx=4)
        ttk.Button(controls, text="Next", command=self.play_next).pack(side="left", padx=4)

        ttk.Label(controls, text="Volume").pack(side="left", padx=(12, 6))
        self.vol_scale = ttk.Scale(controls, from_=0, to=100, orient="horizontal", variable=self.vol_var, command=self._on_volume_change, length=160)
        self.vol_scale.pack(side="left")
        self.lbl_vol = ttk.Label(controls, text=f"{int(self.vol_var.get())}%")
        self.lbl_vol.pack(side="left", padx=(6, 0))

        timeline = ttk.Frame(self, padding=(8, 4))
        timeline.pack(fill="x")
        self.elapsed_lbl = ttk.Label(timeline, text="00:00", width=6)
        self.elapsed_lbl.pack(side="left")
        self.pos_var = tk.DoubleVar(value=0.0)
        self.seek = ttk.Scale(timeline, from_=0, to=0, orient="horizontal", variable=self.pos_var, command=self._on_seek_change)
        self.seek.pack(side="left", fill="x", expand=True, padx=8)
        self.remaining_lbl = ttk.Label(timeline, text="-00:00", width=7)
        self.remaining_lbl.pack(side="left")

        status = ttk.Frame(self, padding=6)
        status.pack(fill="x", side="bottom")
        self.status_lbl = ttk.Label(status, text="Ready")
        self.status_lbl.pack(side="left")

    # Shortcuts
    def _bind_shortcuts(self) -> None:
        self.bind("<Control-o>", lambda e: self.open_files())
        self.bind("<Control-s>", lambda e: self.save_playlist())
        self.bind("<Control-q>", lambda e: self._quit())
        self.bind("<Control-l>", lambda e: self.open_playlist_window())
        self.bind("<Control-t>", lambda e: self.open_settings())
        self.bind("<space>", lambda e: self.toggle_pause())

    # Status / About
    def _set_status(self, text: str) -> None:
        self.status_lbl.config(text=text)

    def _show_about(self) -> None:
        AboutWindow(self)

    # Recents
    def add_to_recents(self, path: Path) -> None:
        p = str(path)
        if p in self.recents:
            self.recents.remove(p)
        self.recents.insert(0, p)
        self.recents = self.recents[: self.MAX_RECENTS]
        save_json(RECENTS_FILE, self.recents)
        self.rebuild_recent_menu()

    def open_recent(self, path: Path) -> None:
        if path.exists():
            self.playlist = [str(path)]
            self.current_index = 0
            self._prepare_current_from_index()
            self.play_current()
        else:
            messagebox.showwarning("Missing", f"{path} not found.")
            self.recents = [r for r in self.recents if r != str(path)]
            save_json(RECENTS_FILE, self.recents)
            self.rebuild_recent_menu()

    # Playlist helpers
    def add_to_playlist(self, path: Path) -> None:
        s = str(path)
        if s not in self.playlist:
            self.playlist.append(s)
            if self.current_index == -1:
                self.current_index = 0
                self._prepare_current_from_index()
            if self.playlist_window:
                self.playlist_window.refresh_from_master()

    def remove_from_playlist(self, idx: int) -> None:
        if 0 <= idx < len(self.playlist):
            del self.playlist[idx]
            if self.current_index >= len(self.playlist):
                self.current_index = len(self.playlist) - 1
            if self.playlist_window:
                self.playlist_window.refresh_from_master()

    def open_files(self) -> None:
        filetypes = [("Audio Files", "*.mp3 *.wav *.ogg *.flac *.m4a"), ("All Files", "*.*")]
        paths = filedialog.askopenfilenames(title="Open audio files", filetypes=filetypes, initialdir=str(self._last_open_dir))
        if not paths:
            return
        for p in paths:
            self.add_to_playlist(Path(p))
        if self.playlist_window:
            self.playlist_window.refresh_from_master()

    def open_single_file(self) -> None:
        filetypes = [("Audio Files", "*.mp3 *.wav *.ogg *.flac *.m4a"), ("All Files", "*.*")]
        path = filedialog.askopenfilename(title="Open a single audio file", filetypes=filetypes, initialdir=str(self._last_open_dir))
        if not path:
            return
        p = Path(path)
        self.add_to_recents_and_play(p)

    def add_to_recents_and_play(self, p: Path):
        self.add_to_recents(p)
        self.playlist = [str(p)]
        self.current_index = 0
        self._prepare_current_from_index()
        self.play_current()

    # Apply settings
    def apply_settings_from_config(self, initial: bool = False):
        theme = self.config_data.get("theme", "system").lower()
        try:
            if theme == "dark":
                self.tk_setPalette(background="#2e2e2e", foreground="white")
                self.style.theme_use("clam")
                self.style.configure(".", background="#2e2e2e", foreground="white")
            else:
                self.tk_setPalette(background="SystemButtonFace", foreground="black")
                self.style.theme_use("clam")
        except Exception:
            pass

        # Volume (mixer is initialized in __init__)
        try:
            vol = float(self.config_data.get("last_volume", self.config_data.get("default_volume", 50.0)))
            self.vol_var.set(vol)
            pygame.mixer.music.set_volume(vol / 100.0)
            self.lbl_vol.config(text=f"{int(vol)}%")
        except Exception:
            pass

        # Always on top
        try:
            self.attributes("-topmost", bool(self.config_data.get("always_on_top", False)))
        except Exception:
            pass

    # Save/load playlist
    def save_playlist(self, out_path: Optional[Path] = None) -> None:
        if out_path is None:
            path = filedialog.asksaveasfilename(title="Save Playlist", defaultextension=".vpl",
                                                filetypes=[("VidPlayer Playlist", "*.vpl"), ("JSON", "*.json")])
            if not path:
                return
            out_path = Path(path)
        data = {"paths": self.playlist}
        try:
            out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
            self.config_data["last_playlist_path"] = str(out_path)
            save_json(CONFIG_FILE, self.config_data)
            self._set_status(f"Playlist saved: {out_path.name}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_playlist(self, path: Optional[Path] = None) -> None:
        if path is None:
            path_str = filedialog.askopenfilename(title="Load Playlist",
                                                  filetypes=[("VidPlayer Playlist", "*.vpl"), ("JSON", "*.json"), ("All Files", "*.*")])
            if not path_str:
                return
            path = Path(path_str)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            paths = data.get("paths", [])
            self.playlist = [str(Path(p)) for p in paths if p and Path(p).exists()]
            self.current_index = 0 if self.playlist else -1
            self.config_data["last_playlist_path"] = str(path)
            save_json(CONFIG_FILE, self.config_data)
            if self.current_index != -1:
                self._prepare_current_from_index()
            if self.playlist_window:
                self.playlist_window.refresh_from_master()
            self._set_status(f"Loaded playlist: {path.name}")
        except Exception as e:
            messagebox.showerror("Load Error", str(e))

    # Prepare audio
    def _prepare_current_from_index(self):
        if not (0 <= self.current_index < len(self.playlist)):
            return
        p = Path(self.playlist[self.current_index])
        self.audio_path = p
        self._last_open_dir = p.parent
        try:
            pygame.mixer.music.load(str(p))
            snd = pygame.mixer.Sound(str(p))
            self.audio_len_s = float(snd.get_length())
            self.seek.config(to=self.audio_len_s if self.audio_len_s > 0 else 0)
            self.pos_var.set(self._last_seek_value if self.config_data.get("resume_last", False) else 0.0)
            self.lbl_file.config(text=p.name)
            # Album art
            art_bytes = get_album_art_bytes(p)
            if art_bytes and Image and ImageTk:
                try:
                    img = Image.open(io.BytesIO(art_bytes))
                    img.thumbnail((96, 96))
                    self._art_photo = ImageTk.PhotoImage(img)
                    self.art_canvas.config(image=self._art_photo)
                except Exception:
                    self._art_photo = None
                    self.art_canvas.config(image="")
            else:
                # if there's an externally provided image for this file persisted, use that small thumbnail
                ext = self.external_art_map.get(str(p))
                if ext and Image and ImageTk and Path(ext).exists():
                    try:
                        img = Image.open(ext)
                        img.thumbnail((96, 96))
                        self._art_photo = ImageTk.PhotoImage(img)
                        self.art_canvas.config(image=self._art_photo)
                    except Exception:
                        self._art_photo = None
                        self.art_canvas.config(image="")
                else:
                    self._art_photo = None
                    self.art_canvas.config(image="")
            self.btn_play.config(state="normal")
            self.btn_pause.config(state="disabled", text="Pause")
            self.btn_stop.config(state="disabled")
            self._set_status("Loaded")
        except Exception as e:
            self._set_status(f"Failed to load: {e}")
            messagebox.showerror("Open Error", str(e))

    def play_current(self):
        if not (0 <= self.current_index < len(self.playlist)):
            return
        if not self.audio_path:
            self._prepare_current_from_index()
        try:
            pygame.mixer.music.play(start=self.pos_var.get())
            pygame.mixer.music.set_volume(self.vol_var.get() / 100.0)
            self._paused = False
            self.btn_pause.config(state="normal", text="Pause")
            self.btn_stop.config(state="normal")
            self._set_status("Playing")
            if self.playlist_window:
                self.playlist_window.refresh_from_master()
                # Update Discord presence if enabled
                if self.rpc:
                    try:
                        self.rpc.update(details=self.audio_path.name, state=f"{APP_NAME}", large_image="vidplayer_logo", large_text=self.audio_path.name,
                                        start=int(time.time()), end=(int(time.time()) + int(self.audio_len_s) if self.audio_len_s else None))
                    except Exception:
                        pass
        except Exception as e:
            messagebox.showerror("Playback Error", str(e))

    def play_index(self, idx: int):
        if idx < 0 or idx >= len(self.playlist):
            return
        self.current_index = idx
        self._last_seek_value = 0.0
        self._prepare_current_from_index()
        self.play_current()

    def play_next(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self._last_seek_value = 0.0
        self._prepare_current_from_index()
        self.play_current()

    def play_previous(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self._last_seek_value = 0.0
        self._prepare_current_from_index()
        self.play_current()

    def toggle_pause(self):
        try:
            if self._paused:
                pygame.mixer.music.unpause()
                self._paused = False
                self.btn_pause.config(text="Pause")
                self._set_status("Playing")
            else:
                pygame.mixer.music.pause()
                self._paused = True
                self.btn_pause.config(text="Resume")
                self._set_status("Paused")
        except Exception:
            pass

    def stop_audio(self):
        try:
            pygame.mixer.music.stop()
            if self.rpc:
                try:
                    self.rpc.update(details="Idle", state=f"{APP_NAME} {VERSION}", large_image="vidplayer_logo", large_text=APP_NAME)
                except Exception:
                    pass
        finally:
            self.pos_var.set(0.0)
            self._paused = False
            self.btn_pause.config(text="Pause", state="disabled")
            self.btn_stop.config(state="disabled")
            self._set_status("Stopped")

    # Volume change callback
    def _on_volume_change(self, _=None):
        v = max(0.0, min(100.0, float(self.vol_var.get())))
        self.lbl_vol.config(text=f"{int(v)}%")
        try:
            pygame.mixer.music.set_volume(v / 100.0)
        except Exception:
            pass
        self.config_data["last_volume"] = float(v)
        save_json(CONFIG_FILE, self.config_data)

    # Seek handling
    def _on_seek_change(self, _=None):
        self._last_seek_value = float(self.pos_var.get())
        if not hasattr(self, "_seek_bindings"):
            self._seek_bindings = True
            self.seek.bind("<ButtonPress-1>", self._begin_scrub, add="+")
            self.seek.bind("<ButtonRelease-1>", self._end_scrub, add="+")

    def _begin_scrub(self, _=None):
        self.user_is_scrubbing = True

    def _end_scrub(self, _=None):
        self.user_is_scrubbing = False
        if not self.audio_path or not pygame.mixer.get_init():
            return
        try:
            was_playing = pygame.mixer.music.get_busy() and not self._paused
            pygame.mixer.music.stop()
            pygame.mixer.music.play(start=self._last_seek_value)
            pygame.mixer.music.set_volume(self.vol_var.get() / 100.0)
            if not was_playing:
                pygame.mixer.music.pause()
                self._paused = True
                self.btn_pause.config(text="Resume")
            self._set_status("Seeked")
        except Exception:
            self._set_status("Seek unsupported for this format")

    # Poll loop
    def _poll(self):
        try:
            position_ms = pygame.mixer.music.get_pos()
        except Exception:
            position_ms = -1
        pos_s = max(0.0, position_ms / 1000.0) if position_ms >= 0 else (self._last_seek_value if self._paused else 0.0)
        if not self.user_is_scrubbing:
            self.pos_var.set(min(pos_s, self.audio_len_s if self.audio_len_s else pos_s))
        self.elapsed_lbl.config(text=format_time(self.pos_var.get()))
        remaining = max(0.0, (self.audio_len_s - self.pos_var.get()) if self.audio_len_s else 0.0)
        self.remaining_lbl.config(text=f"-{format_time(remaining)}")
        try:
            is_busy = pygame.mixer.music.get_busy()
        except Exception:
            is_busy = False
        if self.audio_len_s and not is_busy and not self._paused and self.pos_var.get() >= max(0.5, self.audio_len_s - 0.2):
            if self.config_data.get("auto_play_next", True) and len(self.playlist) > 1:
                self.play_next()
            else:
                self.stop_audio()
        self.after(self.POLL_MS, self._poll)

    # Full screen artwork (modified to add keyboard controls, external artwork selection,
    # minimal overlay player with big play/pause + prev/next + auto-hide on inactivity)
    def open_fullscreen_art(self):
        # If no file loaded, show message
        if not getattr(self, "audio_path", None):
            messagebox.showinfo("Full Screen", "No file loaded to show artwork.")
            return

        # Get embedded bytes; fallback to external_map if present (persisted)
        art_bytes = get_album_art_bytes(self.audio_path) if self.audio_path else None
        external_path = self.external_art_map.get(str(self.audio_path))
        if not art_bytes and external_path:
            try:
                if Path(external_path).exists():
                    art_bytes = Path(external_path).read_bytes()
                else:
                    # remove stale mapping
                    del self.external_art_map[str(self.audio_path)]
                    save_json(ARTMAP_FILE, self.external_art_map)
                    external_path = None
            except Exception:
                art_bytes = None

        # Fullscreen toplevel
        fs = tk.Toplevel(self)
        fs.attributes("-fullscreen", True)
        fs.configure(background="black")
        fs.focus_set()

        # state for update loop
        fs._updater_id = None
        fs._is_scrubbing = False

        # auto-hide overlay state
        overlay_visible = True
        last_motion = time.time()
        hide_after = self.OVERLAY_AUTOHIDE_SEC

        # Close/escape handler
        def close_fs(event=None):
            # cancel scheduled update
            try:
                if fs._updater_id:
                    fs.after_cancel(fs._updater_id)
            except Exception:
                pass
            try:
                fs.destroy()
            except Exception:
                pass

        fs.bind("<Escape>", close_fs)

        # keyboard handlers: left/right/space
        def on_left(ev=None):
            self.play_previous()

        def on_right(ev=None):
            self.play_next()

        def on_space(ev=None):
            self.toggle_pause()

        fs.bind("<Left>", on_left)
        fs.bind("<Right>", on_right)
        fs.bind("<space>", on_space)

        # Show/hide overlay helpers
        def hide_overlay():
            nonlocal overlay_visible
            if overlay_visible:
                try:
                    overlay.place_forget()
                except Exception:
                    pass
                overlay_visible = False

        def show_overlay():
            nonlocal overlay_visible, last_motion
            last_motion = time.time()
            if not overlay_visible:
                try:
                    overlay.place(relx=0.5, rely=0.92, anchor="s")
                except Exception:
                    pass
                overlay_visible = True

        # activity checker
        def check_inactivity():
            nonlocal last_motion
            try:
                if time.time() - last_motion > hide_after:
                    hide_overlay()
            except Exception:
                pass
            fs._updater_id = fs.after(500, check_inactivity)

        # mouse motion handler
        def on_motion(event=None):
            show_overlay()

        fs.bind("<Motion>", on_motion)

        # container
        container = tk.Frame(fs, bg="black")
        container.pack(expand=True, fill="both")

        # area for artwork
        art_label = tk.Label(container, bg="black")
        art_label.pack(expand=True)

        # if no artwork: show message + choose button
        choose_btn = None
        placeholder_txt_widget = None

        def load_and_show_image(bytes_data=None, path=None):
            """Helper: load image (bytes or file path) and display centered and scaled"""
            try:
                if Image is None or ImageTk is None:
                    return False
                if bytes_data:
                    img = Image.open(io.BytesIO(bytes_data))
                elif path:
                    img = Image.open(path)
                else:
                    return False
                sw = fs.winfo_screenwidth()
                sh = fs.winfo_screenheight()
                img_ratio = img.width / img.height
                screen_ratio = sw / sh
                if img_ratio > screen_ratio:
                    target_w = int(sw * 0.9)
                    target_h = int(target_w / img_ratio)
                else:
                    target_h = int(sh * 0.9)
                    target_w = int(target_h * img_ratio)
                img = img.resize((max(1, target_w), max(1, target_h)), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                art_label.config(image=photo)
                art_label.image = photo  # keep ref
                return True
            except Exception:
                return False

        # if embedded present, show it
        showed = False
        if art_bytes and Image and ImageTk:
            showed = load_and_show_image(bytes_data=art_bytes)
        elif external_path and Image and ImageTk and Path(external_path).exists():
            showed = load_and_show_image(path=external_path)

        if not showed:
            # show placeholder text and a "Choose artwork" button
            placeholder_txt_widget = tk.Label(container, text="No artwork available.", fg="white", bg="black", font=("Segoe UI", 18))
            placeholder_txt_widget.pack(expand=True)
            def choose_external():
                nonlocal placeholder_txt_widget, choose_btn, external_path
                p = filedialog.askopenfilename(title="Choose artwork image", filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All Files", "*.*")])
                if not p:
                    return
                # persist chosen external art for this audio file
                try:
                    self.external_art_map[str(self.audio_path)] = p
                    save_json(ARTMAP_FILE, self.external_art_map)
                    external_path = p
                except Exception:
                    pass
                # remove text and button and show image
                try:
                    placeholder_txt_widget.pack_forget()
                except Exception:
                    pass
                try:
                    choose_btn.pack_forget()
                except Exception:
                    pass
                success = load_and_show_image(path=p)
                if not success:
                    messagebox.showerror("Artwork", "Could not load chosen artwork.")
            choose_btn = ttk.Button(container, text="Choose artwork...", command=choose_external)
            choose_btn.pack(pady=12)

        # clicking artwork toggles pause/play
        art_label.bind("<Button-1>", lambda e: self.toggle_pause())

        # Overlay bottom controls: Prev / big play/pause / Next, seek scale, filename, close button
        overlay = tk.Frame(fs, bg="black")
        overlay.place(relx=0.5, rely=0.92, anchor="s")

        # Prev button
        prev_btn = ttk.Button(overlay, text="⏮", width=4, command=self.play_previous)
        prev_btn.pack(side="left", padx=6)

        # big play/pause
        big_btn_text = tk.StringVar(value="⏵" if self._paused else "⏸")
        big_btn = ttk.Button(overlay, textvariable=big_btn_text, width=5)
        big_btn.pack(side="left", padx=6)

        def big_toggle():
            self.toggle_pause()
            big_btn_text.set("⏵" if self._paused else "⏸")

        big_btn.config(command=big_toggle)

        # Next button
        next_btn = ttk.Button(overlay, text="⏭", width=4, command=self.play_next)
        next_btn.pack(side="left", padx=6)

        # seek slider (fullscreen)
        fs_seek_var = tk.DoubleVar(value=self.pos_var.get())
        fs_seek = ttk.Scale(overlay, from_=0, to=max(1, self.audio_len_s), orient="horizontal", variable=fs_seek_var, length=600)
        fs_seek.pack(side="left", padx=8)

        # bindfs seek interactions
        def fs_begin_scrub(ev=None):
            fs._is_scrubbing = True

        def fs_end_scrub(ev=None):
            fs._is_scrubbing = False
            target = float(fs_seek_var.get())
            # perform seek via stop+play(start=target)
            if not self.audio_path or not pygame.mixer.get_init():
                return
            try:
                was_playing = pygame.mixer.music.get_busy() and not self._paused
                pygame.mixer.music.stop()
                pygame.mixer.music.play(start=target)
                pygame.mixer.music.set_volume(self.vol_var.get() / 100.0)
                if not was_playing:
                    pygame.mixer.music.pause()
                    self._paused = True
                # update UI widgets
                self.pos_var.set(target)
            except Exception:
                pass

        fs_seek.bind("<ButtonPress-1>", fs_begin_scrub, add="+")
        fs_seek.bind("<ButtonRelease-1>", fs_end_scrub, add="+")

        # filename label and close
        fn_label = tk.Label(overlay, text=self.audio_path.name if self.audio_path else "", fg="white", bg="black")
        fn_label.pack(side="left", padx=(8, 6))
        ttk.Button(overlay, text="Close (Esc)", command=close_fs).pack(side="left", padx=6)

        # updater: sync fs_seek_var with main pos_var (and update big play/pause icon)
        def updater():
            nonlocal last_motion
            try:
                # Only update UI when not scrubbing inside fullscreen
                if not fs._is_scrubbing:
                    fs_seek_var.set(self.pos_var.get())
                big_btn_text.set("⏵" if self._paused else "⏸")
            except Exception:
                pass
            fs._updater_id = fs.after(200, updater)

        # start updater and inactivity checker
        fs._updater_id = fs.after(200, updater)
        fs.after(500, check_inactivity)

        # ensure keyboard focus goes to fullscreen (so keys work)
        fs.focus_force()

    # Playlist / settings UI
    def open_playlist_window(self):
        if self.playlist_window is None or not tk.Toplevel.winfo_exists(self.playlist_window):
            self.playlist_window = PlaylistWindow(self)
        else:
            self.playlist_window.deiconify()
            self.playlist_window.lift()
        # make sure playlist window shares the same rpc handle
        if self.playlist_window:
            self.playlist_window.rpc = self.rpc
            self.playlist_window.refresh_from_master()

    def open_settings(self):
        SettingsWindow(self)

    # Quit (cleanup)
    def _quit(self):
        try:
            if self.config_data.get("resume_last"):
                self.config_data["last_index"] = int(self.current_index if self.current_index is not None else 0)
                self.config_data["last_position"] = float(self.pos_var.get() if hasattr(self, "pos_var") else 0.0)
            self.config_data["last_volume"] = float(self.vol_var.get())
            save_json(CONFIG_FILE, self.config_data)
        except Exception:
            pass
        try:
            # persist external art map
            save_json(ARTMAP_FILE, self.external_art_map)
        except Exception:
            pass
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except Exception:
            pass
        # clear RPC if exists
        if self.rpc:
            try:
                self.rpc.clear()
            except Exception:
                pass
            try:
                self.rpc.close()
            except Exception:
                pass
            self.rpc = None
        self.destroy()

    # Helper: add_to_recents wrapper used earlier
    def add_to_recents(self, path: Path) -> None:
        p = str(path)
        if p in self.recents:
            self.recents.remove(p)
        self.recents.insert(0, p)
        self.recents = self.recents[: self.MAX_RECENTS]
        save_json(RECENTS_FILE, self.recents)
        self.rebuild_recent_menu()


def main() -> int:
    app = VidPlayerApp()
    app.mainloop()
    # Cleanup RPC if any
    try:
        if app.rpc:
            app.rpc.close()
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    main()
