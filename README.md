# VidPlayer

![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge)
![C%23 Rebuild](https://img.shields.io/badge/C%23%20Rebuild-.NET%2010%20%2F%20WPF-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
![Python Edition](https://img.shields.io/badge/Python%20Edition-3.13.9%20%2F%20PySide6-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Playback](https://img.shields.io/badge/Playback-LibVLC%20%2F%20VLC-FF8800?style=for-the-badge&logo=vlcmediaplayer&logoColor=white)
![License](https://img.shields.io/badge/Source-Available-00A86B?style=for-the-badge)

VidPlayer is a portable Windows audio-player project by **sonic Fan Tech / sonic Fan Games**. The project now has two separate codebases:

- **VidPlayer C# Rebuild** — the current complete C# / WPF / .NET 10 rebuild and the recommended edition for modern Windows x64 systems.
- **VidPlayer Python Edition** — the original Python / PySide6 edition preserved in this repository with its own releases, source history, experiments, and older build line.

The two editions are intentionally maintained in separate repositories so their source code, build systems, dependencies, issues, and release histories do not get mixed together.

---

## Choose an Edition

| Edition | Status | Technology | Best for | Links |
|---|---|---|---|---|
| **VidPlayer C# Rebuild — v2.0.9.2 CS V1.0** | Current complete rebuild | C#, WPF, .NET 10, LibVLCSharp | Windows 10/11 x64 users who want the newest rebuilt application suite | [Repository](https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild) · [Download Build](https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild/releases/download/v2.0.9.2-cs-v1.0/VidPlayer-v2.0.9.2-CS-V1.0-Build.zip) · [Download Source](https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild/releases/download/v2.0.9.2-cs-v1.0/VidPlayer-v2.0.9.2-CS-V1.0-source.zip) |
| **VidPlayer Python Edition — v2.0.9.3.1.1 Beta X64** | Original edition / separate legacy line | Python 3.13.9, PySide6, python-vlc | Users preserving or developing the original Python implementation | [This Repository](https://github.com/sonicFanTech/vidplayer) · [Python Releases](https://github.com/sonicFanTech/vidplayer/releases) |

### Recommended modern download

**VidPlayer C# Rebuild v2.0.9.2 — CS V1.0**

- **Repository:** <https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild>
- **Precompiled build:** <https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild/releases/download/v2.0.9.2-cs-v1.0/VidPlayer-v2.0.9.2-CS-V1.0-Build.zip>
- **Source package:** <https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild/releases/download/v2.0.9.2-cs-v1.0/VidPlayer-v2.0.9.2-CS-V1.0-source.zip>
- **Release page:** <https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild/releases/tag/v2.0.9.2-cs-v1.0>

---

## VidPlayer C# Rebuild

The C# edition is not a thin launcher, wrapper, or partial port. It is a full application-suite rebuild of VidPlayer using **C#**, **WPF**, and **.NET 10** for Windows x64.

### Applications included

| Application | Purpose |
|---|---|
| `VidPlayer.exe` | Main portable audio player |
| `VidPlayerUpdater.exe` | External update installation and rollback manager |
| `VPTheme.Editor.exe` | C# / WPF theme creation, editing, packaging, and preview tool |
| `VPTheme_ThemeEnvironmentTester.exe` | Protected mock VidPlayer environment used to test themes before saving or installing them |
| `VPACDRipper.exe` | C# / WPF Audio CD ripping utility using the BASSCD/BASSenc engine |

### Main C# rebuild highlights

- Portable LibVLC / LibVLCSharp playback.
- AAC, FLAC, M4A, MP3, OGG, WAV, and WMA opening support.
- Play, pause/resume, stop, previous, next, seek, autoplay-next, and session restoration.
- Standalone and docked playlist modes.
- Left, right, top, bottom, and visualizer-tab playlist docking.
- Playlist add, remove, reorder, search, drag-and-drop, save, load, unload, and clear operations.
- Bulk playlist loading with progress, counts, current-file display, filtering, and cancellation.
- Embedded and external artwork support with portable artwork mappings.
- Full Screen Artwork, Full Screen Visualizer, Mini Visualizer, and Mini Mode.
- Multi-file File Info with tags, codec information, artwork, filesystem details, and raw `ffprobe` output.
- LRC, SRT, WebVTT, ASS, and SSA subtitle/lyrics support.
- Bars, waveform, Windows XP Media Player-style blobs, and spectrogram visualizers.
- Real LibVLC PCM callback analysis with safe native signed-16-bit PCM handling.
- Position-synchronized FFmpeg visualizer analysis and fallback data.
- Built-in Light, Dark, System Default, and SteamLike appearance choices.
- Full VPTheme support for colors, gradients, fonts, icons, sounds, menus, dialogs, playlists, tabs, sliders, progress bars, and other WPF controls.
- Multi-language interface and localized document loading.
- Remembered window size, position, maximized state, scaling, and playlist-docking state.
- Configurable 75%–150% interface scaling.
- Discord Rich Presence using the built-in VidPlayer application ID.
- Audio CD playlist creation and direct CDDA playback.
- External C# updater with channels, package verification, protected portable files, and rollback snapshots.

### VPTheme Editor and Theme Environment Tester

The original Python theme editor has been rebuilt in C# and WPF.

VPTheme Editor supports:

- New, Open, Save, Save As, and Duplicate operations.
- Unsaved-change warnings.
- Theme-folder discovery, searching, and refreshing.
- Dark, Light, and SteamLike starter themes.
- Schema-driven editing of roughly 170 theme properties.
- Main Window, Settings, Playlist, and About previews.
- Color, gradient, number, boolean, font, icon, sound, and asset editing.
- Self-contained custom theme folders containing `Theme.vptheme`, `Sounds`, `Icons`, and `Fonts`.
- **Test Run Theme**, which launches `VPTheme_ThemeEnvironmentTester.exe` with the currently edited theme—including unsaved changes.

The Theme Environment Tester displays mock versions of VidPlayer's main window and subwindows. It can show loaded filenames and playlist items, but it does not initialize LibVLC or play audio. It is protected against normal standalone launching and requires a valid active VPTheme Editor session.

### VPACDRipper

The old Win32 Audio CD ripping UI has been replaced by a C# / WPF application while retaining the native BASSCD ripping engine.

VPACDRipper includes:

- Optical-drive and Audio CD detection.
- Track enumeration and duration reading.
- CD-Text album, artist, title, and track metadata.
- Editable track title and artist values.
- Per-track selection, Check All, and Clear All.
- WAV PCM, FLAC, and MP3 ripping.
- Rip Selected and Rip All.
- Per-track and overall progress.
- Cancellation and safe deletion of incomplete output files.
- Portable `AudioCDRipTool.ini` settings.
- Dark, Light, and System appearance choices.
- Default integration with VidPlayer's `Ripped CDA` directory.

---

## Python Edition in This Repository

This repository remains the home of the original Python / PySide6 implementation. It is preserved separately rather than being overwritten by the C# source.

### Python edition status

**Current Python public branch:** `v2.0.9.3.1.1 Beta X64`

The Python edition includes the original implementation of:

- Portable VLC playback through `python-vlc`.
- PySide6 / Qt windows and dialogs.
- Playlist management, search, drag-and-drop, and docking.
- Artwork extraction and Full Screen Artwork mode.
- File Info and metadata display.
- Subtitle and lyrics support.
- Visualizer modes and experimental callback analysis.
- VPTheme colors, fonts, icons, sounds, and packaged theme assets.
- `.langu` multi-language files.
- Discord Rich Presence through `pypresence`.
- Python updater and rollback workflow.
- Experimental Audio CD playback and ripping integrations.

The Python edition remains useful for source-history preservation, experimentation, comparison with the rebuild, and users who specifically prefer the original application.

---

## Screenshots

The screenshots stored in this repository primarily show the Python edition and its earlier theme/UI work.

![VidPlayer Main Window](./Screenshots/Modern/MainWindow.png)
![VidPlayer Playlist Window](./Screenshots/Modern/PlayListWindow.png)
![VidPlayer Settings Window Tab 1](./Screenshots/Modern/SettingsWindow.png)
![VidPlayer Settings Window Tab 2](./Screenshots/Modern/SettingsWindow2.png)
![VidPlayer Settings Window Tab 3](./Screenshots/Modern/SettingsWindow3.png)
![VidPlayer Settings Window Tab 4](./Screenshots/Modern/SettingsWindow4.png)
![VidPlayer File Info Window](./Screenshots/Modern/InfoWindow.png)
![VidPlayer Audio CD Ripping Tool](./Screenshots/Modern/VPEACDRippingTool.png)

C# rebuild screenshots and documentation are maintained in the separate C# repository.

---

## Supported Audio Formats

The main open-file list used by the current C# rebuild includes:

- `.aac`
- `.flac`
- `.m4a`
- `.mp3`
- `.ogg`
- `.wav`
- `.wma`

Actual decoding support can also depend on the bundled LibVLC/VLC runtime and the media file itself.

---

## Portable C# Release Layout

A typical C# release has the following structure:

```text
VidPlayer\
├─ VidPlayer.exe
├─ VidPlayer.Core.dll
├─ VidPlayer.Discord.dll
├─ VidPlayer.Infrastructure.dll
├─ VidPlayer.Localization.dll
├─ VidPlayer.Media.dll
├─ VidPlayer.Playback.dll
├─ VidPlayer.Playback.LibVLC.dll
├─ VidPlayer.Playlists.dll
├─ VidPlayer.Theming.dll
├─ VidPlayer.Visualizers.dll
├─ FEATURES.txt
├─ README.md
├─ RELEASE.md
├─ LICENSE.txt
├─ config.json
├─ recents.json
├─ artmap.json
├─ visualizer_presets.json
├─ Logs\
├─ Ripped CDA\
├─ bin\
│  ├─ ffmpeg.exe
│  ├─ ffprobe.exe
│  ├─ icons\
│  ├─ Langu\
│  ├─ VLCLibs\
│  ├─ VPACDRipper.exe
│  ├─ bass.dll
│  ├─ basscd.dll
│  ├─ bassenc.dll
│  ├─ bassenc_flac.dll
│  ├─ bassenc_mp3.dll
│  └─ VPThemes\
│     ├─ VPTheme.Editor.exe
│     ├─ VPTheme_ThemeEnvironmentTester.exe
│     ├─ Default\
│     └─ custom themes...\
└─ update\
   ├─ VidPlayerUpdater.exe
   ├─ VidPlayer.Core.dll
   ├─ VidPlayer.Infrastructure.dll
   ├─ 7z.exe
   ├─ updater_settings.json
   └─ rollbacks\
```

Keep `VPACDRipper.exe` beside its five native BASS DLLs. Keep `VPTheme_ThemeEnvironmentTester.exe` beside `VPTheme.Editor.exe`.

---

## Running the Python Source

A prebuilt Python release does not require a separately installed Python environment. These instructions are only for running or modifying the source in this repository.

### Requirements

- Python 3.13.9 x64
- PySide6
- pygame
- mutagen
- Pillow
- requests
- pypresence
- python-vlc
- numpy
- py7zr

Install the Python packages:

```bash
pip install PySide6 pygame mutagen Pillow requests pypresence python-vlc numpy py7zr
```

Run VidPlayer:

```bash
python vidplayer.py
```

Open a file from the command line:

```bash
python vidplayer.py "D:\\Music\\song.mp3"
```

Example PyInstaller build:

```bash
pyinstaller --noconfirm --onefile --windowed vidplayer.py
```

The original source can also be edited with [SFT pyIDE](https://sonicfantech.org/Site/pyIDE/index.html).

---

## Building the C# Rebuild

The C# source and its build instructions are in the separate repository:

<https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild>

The repository contains `Build-Release.cmd`, `Build-Release.ps1`, the main solution, the component projects, and the companion-tool solution. The precompiled release is self-contained and does not require users to install a separate .NET runtime.

---

## Migration Notes

- The C# rebuild keeps the established portable folder design.
- Existing `config.json`, `recents.json`, `artmap.json`, `visualizer_presets.json`, updater settings, `.vpl` playlists, `.vptheme` themes, and `.langu` language files are intended to remain compatible where supported.
- Keep a backup before copying user data between editions.
- Do not overwrite the Python installation with the C# build. Extract the C# edition to a separate folder first.
- The C# edition uses a built-in Discord Application ID; the old editable ID field is no longer required.
- The C# Theme Environment Tester is a visual testing tool, not a second audio player.

---

## Project Links

### C# rebuild

- Repository: <https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild>
- Build: <https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild/releases/download/v2.0.9.2-cs-v1.0/VidPlayer-v2.0.9.2-CS-V1.0-Build.zip>
- Source: <https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild/releases/download/v2.0.9.2-cs-v1.0/VidPlayer-v2.0.9.2-CS-V1.0-source.zip>

### Python edition

- Repository: <https://github.com/sonicFanTech/vidplayer>
- Releases: <https://github.com/sonicFanTech/vidplayer/releases>
- Main feature/build log: [CHANGELOG.md](./CHANGELOG.md)
- Update ideas: [UPDATE_IDEAS.md](./UPDATE_IDEAS.md)

### Other

- Developer: <https://github.com/sonicFanTech>
- Update package source: <https://github.com/sonicFanTech/customSetupInstallersPackageDownloads/releases>

---

## Technology Summary

### C# rebuild

- **Language:** C#
- **UI:** WPF
- **Runtime:** .NET 10 for Windows x64
- **Playback:** LibVLCSharp with portable LibVLC/VLC files
- **Metadata:** TagLibSharp and `ffprobe`
- **Visualizer:** C# FFT/PCM processing with LibVLC callbacks and FFmpeg fallback
- **Discord:** DiscordRPC integration
- **CD ripping:** BASSCD and BASSenc native libraries through C# interop

### Python edition

- **Language:** Python 3.13.9
- **UI:** PySide6 / Qt
- **Playback:** `python-vlc` with portable VLC files
- **Metadata:** mutagen
- **Artwork:** Pillow
- **Discord:** pypresence
- **Visualizer:** numpy
- **Updater extraction:** py7zr with external 7-Zip fallback support

---

## Credits

Developed by **sonic Fan Tech / sonic Fan Games**.

VidPlayer also relies on and acknowledges the projects and runtimes used by each edition, including VLC/LibVLC, LibVLCSharp, .NET, WPF, Python, PySide6/Qt, FFmpeg, TagLibSharp, Discord RPC libraries, BASS/BASSCD/BASSenc, 7-Zip, and the other dependencies distributed or referenced by their respective builds.

- Developer profile: <https://github.com/sonicFanTech>
- Python repository: <https://github.com/sonicFanTech/vidplayer>
- C# rebuild repository: <https://github.com/sonicFanTech/VidPlayer-CSharp-Rebuild>
