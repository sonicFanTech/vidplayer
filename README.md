About VidPlayer
===============
VidPlayer is a fast, clean audio player for Windows built with **Python + PySide6**.  
It focuses on the essentials—playlists, drag-and-drop, double-click to play—and a nostalgic **Windows 7-style Aero Glass** theme wrapped in a modern UI.

VidPlayer includes:

- Full-screen artwork view
- Detailed file info
- Recent files
- Discord Rich Presence (optional)
- In-app updater that can download any release asset (EXE/ZIP/7z/etc.) with a progress bar
- Experimental **Audio CD playback & ripping** support

---

Highlights
----------
- Windows 7-style **Aero Glass theme** (with proper enable/disable logic)
- Drag & drop files into the main window or playlist
- Double-click to play:
  - Open files directly when VidPlayer is associated with audio types
  - Or pass a file via command line to VidPlayer.exe
- Batch add dialog for large imports (shows each file + progress, auto-closes)
- Playlist save/load (`.vpl` / JSON)
- Full-screen artwork view with transport controls
- File Info dialog (length, bitrate, tags, dates, size, location, artwork)
- Recent Files menu (with automatic cleanup)
- Discord Rich Presence toggle in Settings
- In-app updater:
  - Checks GitHub Releases
  - Can download **any** asset type directly with a progress bar
- All config/data (`config.json`, `recents.json`, `artmap.json`) saved next to the EXE when bundled (PyInstaller-safe)

Supported formats
-----------------
- **Audio formats:** `.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.aac`, `.wma`  
  (Availability of features like precise seeking may vary by format/codec.)

Audio CD Support (NEW in v2.0.9 BETA 4.2)
-----------------------------------------
VidPlayer can now work with **Audio CDs** in two ways:

1. **Option 1 – Rip Audio CD to files**
   - Uses `cdda2wav` (preferred) or `cdparanoia` if available.
   - Rips tracks into a temporary folder and saves them into a **`Ripped CDA`** folder next to VidPlayer.
   - Lets you choose an output format:
     - WAV (PCM)
     - MP3 (LAME)
     - OGG (Vorbis)
     - FLAC (lossless)
   - If a compressed format is chosen, VidPlayer uses **ffmpeg** (from `bin/ffmpeg.exe` or system PATH) to transcode.
   - Progress dialogs for:
     - Ripping from the CD drive
     - Converting tracks with ffmpeg
   - Option to automatically add the ripped tracks to the current playlist.
   - Temporary `.inf` files created by `cdda2wav` are cleaned up after ripping.

2. **Option 2 – Play Audio CD directly with VLC (experimental)**
   - Uses **python-vlc** + local VLC libraries (`bin/VLCLibs`).
   - Opens a small Audio CD dialog with **Play / Pause / Stop** controls.
   - Completely separate from the main playlist playback.
   - Controlled by a setting: **“Use VLC for Audio CD playback (experimental)”**.
   - When enabled, “Play Audio CD…” uses VLC playback instead of ripping.

**Note:**  
You must provide the external tools yourself:

- `cdda2wav.exe` (or `cdparanoia`) in the `bin` folder or in your PATH  
- `ffmpeg.exe` in `bin` or in your PATH (for MP3/OGG/FLAC output)  
- VLC runtime DLLs in `bin/VLCLibs` for VLC-based Audio CD playback  
- `python-vlc` installed for the .py version

---

Themes & Settings
-----------------
**Themes:**

- Light
- Dark
- System Default
- Aero Glass

**Aero Glass:**

- The “Enable Aero Glass effect” checkbox only applies when the **Aero Glass** theme is selected.
- When enabled, the main window uses a Windows-7-style glass look with gradients and rounded corners.

**Other options:**

- Always on top
- Autoplay next track in playlist
- Resume last track & position on startup
- Auto-load last playlist on startup
- Discord Rich Presence (on/off)
- Use VLC for Audio CD playback (experimental)
- Clear Recent Files

---

Install / Run (Source Version)
==============================
You only need this section if you want to run the **.py** source directly.  
If you’re using the pre-built EXE from Releases, you don’t need Python installed.

### 1. Install Python

VidPlayer is currently targeted at **Python 3.13.9 x64**.

Download Python 3.13.9 x64 from:

- https://www.python.org/ftp/python/3.13.9/python-3.13.9-amd64.exe

During installation:

1. **On the first screen:**
   - Check:
     - “Add python.exe to PATH”
     - “Use admin privileges when installing py.exe”
   - Choose **“Customize installation”**.
2. **On the Optional Features screen:**
   - Leave all checkboxes enabled, then click **Next**.
3. **On the Advanced Options screen:**
   - Check **“Install for all users”**.
   - Leave the three checkboxes underneath it enabled.
   - (Optional) Enable any extra checkboxes you want; they won’t break anything.

### 2. Install required Python packages

Open **Command Prompt** and run:

bash
----
pip install PySide6 pygame mutagen Pillow requests pypresence python-vlc

python-vlc is optional but required for VLC-based Audio CD playback.

3. Run VidPlayer from source
----------------------------
From Command Prompt, in the folder where your .py file is:

python vidplayer_v2.0.9-BETA4_2.py

(Replace the filename with whatever your source file is named.)

You can also pass a file on the command line:
python vidplayer_v2.0.9-BETA4_2.py "D:\Music\song.mp3"


Build Source Code to .EXE
-------------------------
A helper Python compiler tool (written for Python 3.13.9) is included.
It wraps PyInstaller and makes it easier to build 32-bit or 64-bit EXEs.

From Command Prompt:

python pybuilder.py

Commands
--------
help, ?                   Show this help text
list                      Show discovered Python installations
active                    Show active Python (the Python running this script)

build <script> [opts]     Build .py -> .exe

  Options:
    --python <ver_or_path>   Python identifier (e.g. 3.8, 3.13) or full path to python.exe
    --arch x86|x64           Target architecture (must match the interpreter)
    --icon <path>            Optional .ico file
    --name <exename>         Output exe name
    -c                       Show pip install output (verbose)
    -BC                      Show build output from PyInstaller

install_py <version> [x86|x64]   Download & install Python (Windows only)
check_pyinstaller <python>      Check/install PyInstaller for the chosen interpreter

run <commandline>               Run an arbitrary shell command
exit, quit                      Exit this tool


Examples
--------
build myscript.py --python 3.8 --arch x86 --icon C:\icon.ico
python pybuilder.py build myscript.py --python "C:\Python38-32\python.exe" --arch x86

Quick Start
-----------
- Open Files… or drag & drop audio files into the main window or playlist.
- Save/Load playlists (.vpl / JSON) from the File/Playlist dialogs.
- Double-click an audio file (if associated with VidPlayer) or run:
- VidPlayer.exe "path\to\file.mp3"
- View → Full Screen Artwork for an immersive now-playing view.
- File → Play Audio CD… to rip or play an Audio CD (depending on your settings).
- Help → Check for Updates… to open the Releases page or download the latest version in-app with a progress bar.


Tech
----
- UI: Python + PySide6 (Qt)
- Audio playback: pygame
- Tags / metadata: mutagen
- Artwork extraction: Pillow
- Updater / GitHub releases: requests
- Discord integration: pypresence
- Audio CD (optional):
- External cdda2wav / cdparanoia
- External ffmpeg for transcoding
- python-vlc + VLC DLLs for experimental Audio CD playback


Features / Update / Fixes Log
-----------------------------
v2.0.0 – Program rewritten for Python 3.12+

Major internal rework of the player.

v2.0.1 – UI refresh & new basics

Player UI redesigned again.

Added Light/Dark mode.

Added Recent Files list.

v2.0.2 – Artwork & Playlists

Added embedded artwork display.

Added Settings window.

Reworked volume slider (temporarily broke it).

Added playlist support.

v2.0.3 – Auto-play (broken, unreleased)

First attempt at auto-play next file in playlist.

Build was not working and was never publicly released.

v2.0.4 – Auto-play fixed

Fixed auto-play next track behavior.

Added more options to the Settings window.

v2.0.5 – Batch-loading progress window

Added a progress/loading window that appears when opening more than 10 files.

v2.0.6 – New About window

Added a new About window.

v2.0.6.1 – License & update system improvements

Updated License Agreement.

License and Features/Update Log tabs now load text from external files (no hard-coded text).

Added auto-check for updates on startup.

Added a “Check for updates” button to the About menu.

v2.0.7 – Discord RPC

Added Discord Rich Presence integration.

Changed default volume to 50.0.

v2.0.8 – Fullscreen artwork & new settings

Added a Discord Rich Presence toggle in Settings (enable/disable at runtime).

App now maintains a single RPC connection shared with the playlist window.

Added an “Always on top” setting in Settings.

Added Full Screen entry (fullscreen artwork) to the Tools menu:

Escape to exit fullscreen

Clicking artwork toggles play/pause

Small label showing filename + close button

All new settings are saved to config.json and loaded at startup.

v2.0.8.1 – Artwork persistence & overlay improvements

External artwork paths are now persisted in artmap.json and restored across restarts.

Added Prev/Next buttons in the fullscreen overlay.

Overlay auto-hides after a few seconds of inactivity and reappears on mouse move.

Kept the “choose external artwork when embedded missing” flow and made it persist immediately.

v2.0.9 BETA 1 – PySide6 / Qt GUI + File Info

Replaced the old Tkinter GUI with a PySide6 (Qt) GUI.

Note: new GUI was designed for Windows 11; visuals may differ on Windows 10.

Added a File Info tool under the Tools menu showing:

File name, type/extension, size (KB/MB), full path

Creation & modification date/time

Artist, album, year (if available)

Track length, bitrate (if available)

Copyright tag

Embedded or external artwork (or “No artwork found”)

Moved Full Screen Artwork from Tools → View menu (shortcut behavior unchanged).

Added a new Aero Glass theme inspired by Windows 7 Aero effects.

v2.0.9 BETA 2–3

No public update/fix log recorded for these builds.

v2.0.9 BETA 4 – Polishing the new UI

“Enable Aero Glass” checkbox correctly disabled unless theme is set to Aero.

Full Screen Artwork confirmed under the View menu.

Re-added update downloader with progress dialog.

Fixed crashes caused by unsupported Qt stylesheet properties.

Fixed Save/Load QAction triggers.

v2.0.9 BETA 4.1 – Updater & batch-add upgrades, x64/x86 builds

Fixed updater freeze/crash at 100% by safely cleaning up worker threads.

Updater can now download any asset type from GitHub releases (no extension filtering).

JSON files (config.json, recents.json, artmap.json) are now always created next to the EXE when compiled (PyInstaller-safe paths).

Drag & Drop / multi-open now uses a progress dialog that:

Lists each file being added

Runs in a background thread

Auto-closes when finished

First VidPlayer release to ship both x64 and x86 builds.

v2.0.9 BETA 4.2 – Audio CD ripping & VLC playback (current)

Added File → Play Audio CD… and a Playlist → “Play Audio CD…” button.

Implemented Audio CD ripping using cdda2wav (preferred) or cdparanoia:

Rips tracks into a timestamped session folder and then into a shared Ripped CDA folder.

Lets you choose output format: WAV, MP3, OGG or FLAC.

Uses local ffmpeg.exe (or system ffmpeg) to transcode when a compressed format is chosen.

Shows progress dialogs for both ripping and converting.

Optionally adds ripped tracks to the current playlist.

Cleans up temporary .inf files created by cdda2wav.

Added optional VLC-based Audio CD playback:

New “Use VLC for Audio CD playback (experimental)” setting in the Settings dialog.

When enabled, “Play Audio CD…” opens a small VLC-backed CD player window (Play/Pause/Stop).

Uses DLLs from bin/VLCLibs and python-vlc.

General stability tweaks around CD detection, SCSI device selection and temporary folder handling.
