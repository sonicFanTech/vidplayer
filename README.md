# VidPlayer

![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.13.9-3776AB?style=for-the-badge&logo=python&logoColor=white)
![UI](https://img.shields.io/badge/UI-PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![Playback](https://img.shields.io/badge/Playback-VLC%203.0.23-FF8800?style=for-the-badge&logo=vlcmediaplayer&logoColor=white)
![Status](https://img.shields.io/badge/Status-Pre--Release-orange?style=for-the-badge)
![Updater](https://img.shields.io/badge/Updater-External%20Python-blue?style=for-the-badge)

A fast, clean Windows audio player built with **Python + PySide6**, with **portable VLC playback**, playlist tools, subtitle / lyrics support, artwork viewing, Discord Rich Presence, and an external updater.

---

## Quick Links

- **Releases:** <https://github.com/sonicFanTech/vidplayer/releases>
- **Developer:** <https://github.com/sonicFanTech>
- **pyIDE:** <https://sonicfantech.org/Site/pyIDE/index.html>
- **Latest update package source:** <https://github.com/sonicFanTech/customSetupInstallersPackageDownloads/releases>
- **Main feature / build log:** [CHANGELOG.md](./CHANGELOG.md)

---

## Screenshots

> Replace these paths if your repo uses a different screenshots folder.

![VidPlayer Main Window](./Screenshots/Modern/MainWindow.png)
![VidPlayer Playlist Window](./Screenshots/Modern/PlayListWindow.png)
![VidPlayer Settings Window](./Screenshots/Modern/SettingsWindow.png)
![VidPlayer File Info Window](./Screenshots/Modern/InfoWindow.png)

---

## Highlights

- Portable **VLC-based playback engine**
- Updated portable VLC runtime DLLs to **VLC 3.0.23**
- Playlist save / load support (`.vpl` / JSON)
- Drag-and-drop audio loading
- Batch add dialog for large file imports
- File Info window with tags, bitrate, dates, size, and artwork
- Full-screen artwork view
- Recent Files menu
- Discord Rich Presence toggle
- Subtitle / lyrics support with styling controls
- Dockable playlist mode
- Mini Mode UI
- Experimental live VLC visualizer data mode
- External updater with hash-based partial updates and rollback manifests
- External Audio CD ripper tool support

---

## Main Features

### Playback
- Portable VLC playback path for the main player
- Double-click to play supported files
- Command-line file opening support
- Resume last file / position support
- Auto-play next track option
- Always-on-top option

### Playlist
- Add, remove, reorder, save, and load playlists
- Search / filter playlist entries
- Dockable playlist mode
- Drag-and-drop support in the main window and playlist UI
- Batch loading dialog for large imports

### Artwork / Info
- Full-screen artwork mode
- Embedded artwork support
- External artwork fallback support
- File Info dialog with metadata and artwork preview

### Subtitles / Lyrics
- Auto-load sidecar subtitle / lyrics files
- Manual subtitle file loading
- Font size, bold, color, background, opacity, and position controls
- Timing offset setting
- Mini Mode-safe subtitle handling

### Visualizer
- Multiple visualizer styles
- Adjustable FPS and size
- Custom color presets / HEX colors
- Experimental live VLC callback visualizer mode

### Audio CD / External Tools
- Audio CD tracks can flow through the main playlist/player path
- External Audio CD ripper tool support
- Preferred ripper executable name: `VPACDRipper.exe`
- Support for local helper tools in `bin\`

### Updater
- External updater workflow
- Python-based updater rework
- Shared updater settings file in `update\updater_settings.json`
- Hash-based partial update logic
- Preserve rules for local files
- Rollback snapshots with manifests
- Auto-launch support back into VidPlayer after update / rollback

---

## Supported Audio Formats

- `.mp3`
- `.wav`
- `.ogg`
- `.flac`
- `.m4a`
- `.aac`
- `.wma`

Some playback behavior can vary depending on codec support inside VLC.

---

## Folder Layout

A typical portable layout looks like this:

```text
VidPlayer\
├─ vidplayer.exe
├─ config.json
├─ recents.json
├─ artmap.json
├─ visualizer_presets.json
├─ bin\
│  ├─ VLCLibs\
│  │  ├─ libvlc.dll
│  │  ├─ libvlccore.dll
│  │  └─ plugins\
│  └─ VPACDRipper.exe
├─ update\
│  ├─ VidPlayerUpdater.exe
│  ├─ VidPlayerUpdater.py
│  ├─ updater_settings.json
│  └─ rollbacks\
└─ Ripped CDA\
```

---

## Run / Edit / Build from Source

This section is only for running the Python source directly. If you are using a prebuilt release, you do **not** need Python installed.

### Requirements

VidPlayer is currently targeted at **Python 3.13.9 x64**.

Download Python:

- <https://www.python.org/ftp/python/3.13.9/python-3.13.9-amd64.exe>

Install required packages:

```bash
pip install PySide6 pygame mutagen Pillow requests pypresence python-vlc numpy py7zr
```

Notes:
- `python-vlc` is needed for VLC Python bindings.
- `numpy` is used for visualizer features.
- `py7zr` is used by the Python updater, with fallback support for external 7-Zip tools when needed.

---

## Using pyIDE (Recommended Source Workflow)

[SFT PyIDE](https://sonicfantech.org/Site/pyIDE/index.html) is your custom Python IDE, and it fits VidPlayer really well because it has a tabbed editor, project file tree, interpreter selection, two run modes, and a built-in PyInstaller compiler window. citeturn235594view0

### What pyIDE is useful for with VidPlayer

- Opening and editing the VidPlayer source in a tabbed editor
- Running VidPlayer inside the IDE output panel
- Running VidPlayer in a real external console when needed
- Choosing which Python interpreter runs the project
- Building EXEs from inside the built-in PyInstaller compiler window citeturn235594view0

### pyIDE setup steps

1. Install Python 3.13.9 x64.
2. Install the VidPlayer Python packages.
3. Open **pyIDE**.
4. Open the VidPlayer source file:
   - `vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed_updater_settings.py`
5. Make sure pyIDE is using the Python interpreter you want.
6. Run VidPlayer using one of pyIDE's run modes:
   - **Run inside PyIDE** for quick testing
   - **Run in external console** if you want a real terminal window citeturn235594view0

### Placeholder screenshots for the pyIDE section

> Add your own screenshots later by replacing these placeholder paths.

![Placeholder - pyIDE main window](./Screenshots/Placeholders/pyIDE_MainWindow_Placeholder.png)
![Placeholder - pyIDE interpreter manager](./Screenshots/Placeholders/pyIDE_InterpreterManager_Placeholder.png)
![Placeholder - pyIDE run from source](./Screenshots/Placeholders/pyIDE_RunVidPlayer_Placeholder.png)
![Placeholder - pyIDE PyInstaller compiler](./Screenshots/Placeholders/pyIDE_PyInstallerCompiler_Placeholder.png)

### Building VidPlayer from source with pyIDE

pyIDE includes a built-in PyInstaller compiler window, so this is the easiest GUI-based way to build VidPlayer into an EXE. citeturn235594view0

Suggested flow:

1. Open VidPlayer in pyIDE.
2. Save any changes.
3. Open pyIDE's **PyInstaller compiler window**.
4. Select the VidPlayer script as the build target.
5. Build the EXE.
6. Copy the finished build into your normal VidPlayer folder layout with:
   - `bin\VLCLibs\`
   - `update\`
   - any other required helper files

### Placeholder screenshots for the build process

![Placeholder - pyIDE open source file](./Screenshots/Placeholders/pyIDE_OpenSource_Placeholder.png)
![Placeholder - pyIDE build settings](./Screenshots/Placeholders/pyIDE_BuildSettings_Placeholder.png)
![Placeholder - pyIDE build output](./Screenshots/Placeholders/pyIDE_BuildOutput_Placeholder.png)

---

## Standard Python / Command Line Workflow

This section keeps the non-pyIDE method too.

### Run VidPlayer from source

```bash
python vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed_updater_settings.py
```

You can also pass a file directly:

```bash
python vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed_updater_settings.py "D:\Music\song.mp3"
```

### Build VidPlayer to EXE with PyInstaller

```bash
pyinstaller --noconfirm --onefile --windowed vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed_updater_settings.py
```

### Build the updater to EXE

```bash
pyinstaller --noconfirm --onefile --windowed VidPlayerUpdater_Python_Reworked_with_settings.py --name VidPlayerUpdater
```

### Placeholder screenshots for the non-pyIDE method

![Placeholder - command prompt install packages](./Screenshots/Placeholders/CMD_InstallPackages_Placeholder.png)
![Placeholder - command prompt run source](./Screenshots/Placeholders/CMD_RunVidPlayer_Placeholder.png)
![Placeholder - command prompt pyinstaller build](./Screenshots/Placeholders/CMD_PyInstallerBuild_Placeholder.png)

---

## Updater Notes

The newer updater system is designed to be safer for portable installs.

It supports:
- remote version checks
- package download
- hash checking
- partial update apply
- local file preserve rules
- updater-folder exclusion
- uninstaller-file exclusion
- rollback snapshots with manifests
- shared settings between VidPlayer and the updater itself

Default local-preserve behavior is intended to avoid replacing user data files like `.json` config files.

---

## Themes / UI Modes

VidPlayer supports:
- Light theme
- Dark theme
- System default theme
- Mini Mode
- Dockable playlist mode

Older Aero Glass-era wording from previous builds has been replaced by the newer portable VLC branch and newer UI workflow.

---

## Tech Stack

- **UI:** PySide6 / Qt
- **Playback:** VLC via portable runtime DLLs
- **Metadata:** mutagen
- **Artwork:** Pillow
- **Requests / updater:** requests
- **Discord integration:** pypresence
- **Visualizer math:** numpy
- **Updater extraction:** py7zr with external 7-Zip fallback support

---

## Current Build Notes

Current README focus:
- newer portable VLC branch
- VLC runtime updated from **3.0.21** to **3.0.23**
- external Python updater rework
- shared updater settings integration
- safer rollback support
- improved Mini Mode / playlist docking / visualizer handling

For the full version history, see [CHANGELOG.md](./CHANGELOG.md).

---
