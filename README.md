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

## Install / Run from Source

This section is only for running the Python source directly. If you are using a prebuilt release, you do **not** need Python installed.

### 1. Install Python

VidPlayer is currently targeted at **Python 3.13.9 x64**.

Download:

- <https://www.python.org/ftp/python/3.13.9/python-3.13.9-amd64.exe>

### 2. Install required packages

```bash
pip install PySide6 pygame mutagen Pillow requests pypresence python-vlc numpy py7zr
```

Notes:
- `python-vlc` is needed for VLC Python bindings.
- `numpy` is used for visualizer features.
- `py7zr` is used by the Python updater, with fallback support for external 7-Zip tools when needed.

### 3. Run VidPlayer from source

```bash
python vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed_updater_settings.py
```

You can also pass a file directly:

```bash
python vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed_updater_settings.py "D:\Music\song.mp3"
```

---

## Build to EXE

If you are building from source, you can use your normal PyInstaller workflow.

Basic example:

```bash
pyinstaller --noconfirm --onefile --windowed vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed_updater_settings.py
```

For the updater:

```bash
pyinstaller --noconfirm --onefile --windowed VidPlayerUpdater_Python_Reworked_with_settings.py --name VidPlayerUpdater
```

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


## Run / Edit / Build from Source

You can work with VidPlayer source in **two ways**:

1. **Recommended: use SFT PyIDE**  
2. **Classic/manual method: use Python + Command Prompt**

---

### Option 1 — Use SFT PyIDE (recommended)

If you want an easier way to **open, edit, run, and build** VidPlayer from source, you can use **SFT PyIDE**, a Python IDE made by sonicFanTech.

PyIDE includes:
- Tabbed Python editor
- Project file manager
- Multiple Python interpreter support
- Run inside the IDE or in a real external console
- Built-in PyInstaller compiler window
- Settings, autosave, and recent files

**PyIDE website:**  
`https://sonicfantech.org/Site/pyIDE/index.html`

#### PyIDE setup steps for VidPlayer

1. Install **Python 3.13.9 x64**.
2. Install the packages VidPlayer needs.
3. Open **PyIDE**.
4. Open the VidPlayer source file.
5. Run the script from inside PyIDE, or use the external console mode.
6. Use PyIDE's built-in compiler window if you want to build an EXE.

#### Packages to install for VidPlayer

```bash
pip install PySide6 pygame mutagen Pillow requests pypresence python-vlc numpy
```

**Optional packages / notes:**
- `python-vlc` is required for the VLC playback/runtime parts.
- `numpy` is used for visualizer-related functionality.
- `py7zr` and `requests` are useful if you also want to run the external updater source.
- `PyInstaller` is needed if you want to build EXEs:

```bash
pip install pyinstaller
```

#### Placeholder screenshots for the PyIDE walkthrough

> Replace these with your real screenshots later.

```text
[Screenshot Placeholder 1: PyIDE main window with VidPlayer source opened]
```

```text
[Screenshot Placeholder 2: PyIDE interpreter selection / run options]
```

```text
[Screenshot Placeholder 3: PyIDE compiler / build window]
```

#### Example PyIDE workflow

- Open `vidplayer_*.py` in PyIDE
- Check that the selected interpreter is your Python 3.13.9 x64 install
- Press **F5** to run inside PyIDE, or use the external console option
- Open the compiler window in PyIDE if you want to build a packaged EXE

---

### Option 2 — Classic / manual method

You only need this section if you want to run the **.py** source directly without PyIDE.  
If you are using the pre-built EXE from Releases, you do **not** need Python installed.

#### 1. Install Python

VidPlayer is currently targeted at **Python 3.13.9 x64**.

Download Python 3.13.9 x64 from the official Python website.

During installation:
- Enable **Add python.exe to PATH**
- Enable **Use admin privileges when installing py.exe**
- Choose **Customize installation**
- Keep the default optional features enabled
- Recommended: install for all users

#### 2. Install required Python packages

Open **Command Prompt** and run:

```bash
pip install PySide6 pygame mutagen Pillow requests pypresence python-vlc numpy
```

#### 3. Run VidPlayer from source

From Command Prompt, in the folder where the source file is:

```bash
python vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed.py
```

You can also pass a file on the command line:

```bash
python vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed.py "D:\Music\song.mp3"
```

#### 4. Build VidPlayer into an EXE

You can build with **PyInstaller** or with your own helper/build tools.

Example PyInstaller install:

```bash
pip install pyinstaller
```

Example build command:

```bash
pyinstaller --noconfirm --onefile --windowed vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed.py
```

#### Placeholder screenshots for the manual method

```text
[Screenshot Placeholder 4: Command Prompt showing pip install]
```

```text
[Screenshot Placeholder 5: Command Prompt showing python vidplayer_*.py]
```

```text
[Screenshot Placeholder 6: PyInstaller build output]
```



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

## Credits

Developed by **sonic Fan Tech / sonic Fan Games**

- GitHub: <https://github.com/sonicFanTech>
- Releases: <https://github.com/sonicFanTech/vidplayer/releases>

