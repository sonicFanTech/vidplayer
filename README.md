# VidPlayer

![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.13.9-3776AB?style=for-the-badge&logo=python&logoColor=white)
![UI](https://img.shields.io/badge/UI-PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![Playback](https://img.shields.io/badge/Playback-VLC%203.0.23-FF8800?style=for-the-badge&logo=vlcmediaplayer&logoColor=white)
![Status](https://img.shields.io/badge/Status-Beta-blue?style=for-the-badge)
![Updater](https://img.shields.io/badge/Updater-External%20Python-blue?style=for-the-badge)

A Windows audio player built with **Python + PySide6**, using **portable VLC playback**, a custom **VPTheme** engine, **multi-language UI support**, **subtitle / lyrics support**, **custom UI sounds**, **custom .ico-based icons**, a built-in **File Info** window, Discord Rich Presence, and an external updater with rollback support.

---

## Quick Links

- **Releases:** <https://github.com/sonicFanTech/vidplayer/releases>
- **Developer:** <https://github.com/sonicFanTech>
- **Update package source:** <https://github.com/sonicFanTech/customSetupInstallersPackageDownloads/releases>
- **Main feature / build log:** [CHANGELOG.md](./CHANGELOG.md)
- **UPDATE IDEAS:** [UPDATE IDEAS](./UPDATE_IDEAS.md)

---

## Current Status

**Current main public branch status:** `v2.0.9.3.1.1 Beta X64`

This Beta build is the first public step forward from the unreleased Experimental branch.

Main Beta focus:
- Multi-language support
- VPTheme engine support in VidPlayer
- UI sound support
- Appearance / theme workflow improvements
- Packaged theme asset support
- Playlist / settings / updater polish

---

## Screenshots

![VidPlayer Main Window](./Screenshots/Modern/MainWindow.png)
![VidPlayer Playlist Window](./Screenshots/Modern/PlayListWindow.png)
![VidPlayer Settings Window Tab 1](./Screenshots/Modern/SettingsWindow.png)
![VidPlayer Settings Window Tab 2](./Screenshots/Modern/SettingsWindow2.png)
![VidPlayer Settings Window Tab 3](./Screenshots/Modern/SettingsWindow3.png)
![VidPlayer Settings Window Tab 4](./Screenshots/Modern/SettingsWindow4.png)
![VidPlayer File Info Window](./Screenshots/Modern/InfoWindow.png)
![VidPlayer Audio CD Ripping Tool](./Screenshots/Modern/VPEACDRippingTool.png)

---

## Highlights

- Portable **VLC-based playback engine**
- Updated portable VLC runtime DLLs to **VLC 3.0.23**
- Custom **.ico-based** button and menu icon system
- Built-in **File Info** window with expanded media / codec details
- Full Screen Artwork mode
- Subtitle / lyrics support
- Dockable playlist mode
- Mini Mode
- External updater with rollback snapshots
- **Multi-language UI support**
- **VPTheme custom theme support**
- **Custom theme fonts / icons / sounds**
- **UI sound support**
- **Appearance tab / theme workflow improvements**

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
- Add, remove, reorder, save, load, unload, and clear playlists
- Search / filter playlist entries
- Dockable playlist mode
- Drag-and-drop support in the main window and playlist UI
- Batch loading dialog for large imports
- Better large-playlist loading workflow

### Artwork / Info
- Full Screen Artwork mode
- Embedded artwork support
- External artwork fallback support
- VPLogo placeholder support when no artwork is available
- File Info dialog with expanded media, container, codec, and artwork details
- Multi-file File Info list support when more than one track is loaded

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

### Themes / Appearance
- Built-in Light / Dark / System Default theme handling
- Custom `.vptheme` support
- Theme reload support in Settings
- Open VPThemes folder button in Settings
- Theme gradients, colors, tabs, inputs, playlist styling, progress bar styling
- Theme font support with file-based loading
- Theme icon override support
- Theme UI sound support
- Appearance settings for UI sounds and volume

### Multi-language Support
- UI language files loaded from `bin\\Langu\\UI\\`
- Localized docs loaded from `bin\\Langu\\Docs\\`
- `.langu` JSON-based language files
- Language selector in Settings
- Reload language files button in Settings
- Fallback handling when language docs or UI files are missing

### Audio CD / External Tools
- Audio CD tracks can flow through the main playlist/player path
- External Audio CD ripper tool support
- Preferred ripper executable name: `VPACDRipper.exe`
- Support for local helper tools in `bin\\`

### Updater
- External updater workflow
- Python-based updater
- Shared updater settings file in `update\\updater_settings.json`
- Hash-based partial update logic
- Preserve rules for local files
- Rollback snapshots with manifests
- Auto-launch support back into VidPlayer after update / rollback
- Build-channel support
- Build-type-aware update logic

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
VidPlayer\\
├─ vidplayer.exe
├─ config.json
├─ recents.json
├─ artmap.json
├─ visualizer_presets.json
├─ bin\\
│  ├─ VLCLibs\\
│  │  ├─ libvlc.dll
│  │  ├─ libvlccore.dll
│  │  └─ plugins\\
│  ├─ icons\\
│  │  ├─ VPLogo.ico
│  │  ├─ buttons\\
│  │  └─ menubar\\
│  ├─ Langu\\
│  │  ├─ UI\\
│  │  └─ Docs\\
│  ├─ VPThemes\\
│  │  ├─ Default\\
│  │  │  ├─ Dark.vptheme
│  │  │  ├─ Light.vptheme
│  │  │  ├─ SystemDefault.vptheme
│  │  │  └─ Sounds\\
│  │  └─ ThemeName\\
│  │     ├─ Theme.vptheme
│  │     ├─ Sounds\\
│  │     ├─ Icons\\
│  │     └─ Fonts\\
│  ├─ ffprobe.exe
│  ├─ ffmpeg.exe
│  └─ VPACDRipper.exe
├─ update\\
│  ├─ VidPlayerUpdater.exe
│  ├─ updater_settings.json
│  ├─ CheckSum.dat
│  └─ rollbacks\\
└─ Ripped CDA\\
```

---

## Install / Run from Source

This section is only for running the Python source directly. If you are using a prebuilt release, you do **not** need Python installed.

### Option A — Use **pyIDE** (recommended for editing / running / building)

If you want a more guided way to work with the VidPlayer source, you can use **SFT pyIDE**, a custom Python IDE.

Links:
- **pyIDE Website:** [SFT pyIDE](https://sonicfantech.org/Site/pyIDE/index.html)
- **GitHub Repository:** [sonicFanTech/pyIDE](https://github.com/sonicFanTech/pyIDE)
- **Releases:** [pyIDE v1.2.0](https://github.com/sonicFanTech/pyIDE/releases/tag/v1.2.0)

#### 1. Install Python
VidPlayer is currently targeted at **Python 3.13.9 x64**.

#### 2. Install required packages

```bash
pip install PySide6 pygame mutagen Pillow requests pypresence python-vlc numpy py7zr
```

#### 3. Run VidPlayer from source

```bash
python vidplayer.py
```

You can also pass a file directly:

```bash
python vidplayer.py "D:\\Music\\song.mp3"
```

#### 4. Build to EXE

```bash
pyinstaller --noconfirm --onefile --windowed vidplayer.py
```

Updater example:

```bash
pyinstaller --noconfirm --onefile --windowed VidPlayerUpdater.py --name VidPlayerUpdater
```

### Option B — Standard Python / Command Prompt workflow

Use the same package list and run/build steps above if you prefer plain Python + Command Prompt instead of pyIDE.

---

## Themes / UI Modes

VidPlayer currently supports:
- Light theme
- Dark theme
- System default theme
- Custom VPThemes
- Mini Mode
- Dockable playlist mode
- Full Screen Artwork mode

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

## Credits

Developed by **sonic Fan Tech / sonic Fan Games**

- GitHub: <https://github.com/sonicFanTech>
- Releases: <https://github.com/sonicFanTech/vidplayer/releases>
