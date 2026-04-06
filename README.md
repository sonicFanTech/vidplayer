# VidPlayer

VidPlayer is a Windows audio player built with **Python + PySide6** with a portable **VLC/libVLC** playback setup.
It focuses on local music playback, playlist handling, artwork, file info, subtitles / lyrics, and a standalone updater workflow.

## Current build

**Version:** `v2.0.9.1.2 Pre-Release X64`

## Highlights

- Portable VLC-based playback using local VLC files from `bin/VLCLibs`
- Drag-and-drop audio loading
- Playlist support with save/load (`.vpl` / JSON)
- Full-screen artwork view
- Detailed file info dialog
- Recent files menu
- Optional Discord Rich Presence
- Subtitle / lyrics support with sidecar auto-load
- FFT / live-data visualizer modes
- Dockable playlist mode
- Mini Mode UI
- External Audio CD ripper tool support
- External updater with rollback support

## Main features

### Playback

- Supports common local audio formats:
  - `.mp3`
  - `.wav`
  - `.ogg`
  - `.flac`
  - `.m4a`
  - `.aac`
  - `.wma`
- Drag & drop files into the main window or playlist
- Double-click to play files when associated with VidPlayer
- Command-line file opening is supported
- Resume last track / position support
- Auto-play next track support
- Always-on-top option

### Playlist

- Add/remove tracks
- Save/load playlists
- Playlist search/filter
- Batch add dialog for large imports
- Dockable playlist mode with multiple docking locations
- Optional playlist docking with the visualizer area

### Artwork / Info

- Embedded artwork support
- External artwork fallback / persistence
- Full-screen artwork window with playback controls
- File Info dialog with:
  - file type
  - size
  - path
  - timestamps
  - artist / album / year
  - bitrate / length
  - artwork preview

### Subtitles / Lyrics

- Enable / disable subtitle display
- Auto-load sidecar subtitle files with the same base filename
- Supported subtitle / lyric sidecar formats:
  - `.lrc`
  - `.srt`
  - `.vtt`
  - `.ass`
  - `.ssa`
- Adjustable font size, bold text, colors, background, opacity, position, and timing offset
- Manual subtitle file loading

### Visualizer

- Optional built-in visualizer
- Multiple styles:
  - Bars
  - Waveform
  - XP WMP-style blobs
  - Spectrogram
- Adjustable FPS and size
- Color presets and custom HEX colors
- Experimental live VLC callback visualizer mode

### Mini Mode / UI

- Mini Mode for a smaller player layout
- Artwork-focused compact UI
- Cleaner overlay / scaling behavior in newer builds
- Docking / subtitle behaviors adjusted so Mini Mode stays cleaner and more stable

### Audio CD support

VidPlayer’s newer builds move Audio CD handling toward the main player flow and an external ripper workflow.

Current behavior includes:

- Audio CD tracks can appear in the playlist flow
- Selected drive handling was improved
- The older built-in rip-first path was removed
- Built-in ripping inside VidPlayer was replaced by an external ripper tool approach

### External Audio CD ripper tool

VidPlayer can launch an external Audio CD ripper tool from the **Tools** menu.

Preferred file name:

- `bin\VPACDRipper.exe`

Compatible fallback names can also be supported if present.

## External updater

VidPlayer now uses an **external updater** instead of the old built-in updater flow.

### Updater features

- Separate updater app stored in `update\`
- Hash-based update comparison
- Checksum / manifest-driven update workflow
- Partial update apply logic
- Real rollback snapshots with manifests
- Auto-launch VidPlayer after update or rollback
- Shared updater settings file used by both VidPlayer and the updater

### Updater safety behavior

The updater was reworked to be safer about what it replaces.

By default it is designed to avoid replacing or deleting:

- the `update\` folder itself
- updater files
- common uninstaller files
- user JSON/config data such as:
  - `config.json`
  - `recents.json`
  - `artmap.json`
  - `visualizer_presets.json`

### Updater settings integration

VidPlayer and the updater share settings through:

- `update\updater_settings.json`

These settings include:

- auto-check for updates
- check every N launches
- auto-open VidPlayer after update / rollback
- close VidPlayer when launching the updater

## Settings

### General

- Theme: Light / Dark / System Default
- Auto-load last playlist on startup
- Resume last track & position
- Auto-play next track
- Always on top
- Discord Rich Presence toggle
- Dockable playlist mode toggle
- Clear Recent Files

### Visualizer

- Enable / disable visualizer
- Live VLC visualizer toggle
- Style selection
- FPS
- Visualizer size
- Color preset / custom HEX color

### Subtitles / Lyrics

- Enable / disable
- Auto-load sidecar file
- Font size
- Bold
- Font color
- Background enable
- Background color
- Background opacity
- Display position
- Timing offset
- Manual subtitle file loader

### Updater

- Auto-check enabled
- Check every N launches
- Auto-open VidPlayer after update / rollback
- Close VidPlayer when launching updater

## Files saved next to the app

VidPlayer stores its local data next to the EXE or script folder:

- `config.json`
- `recents.json`
- `artmap.json`
- `visualizer_presets.json`
- `vidplayer_startup.log`

Updater data lives in the `update\` folder, including:

- `updater_settings.json`
- `updater_state.json`
- `updater_log.txt`
- rollback snapshots

## Source requirements

If you want to run the Python source directly, install Python 3.13 x64 and these packages:

```bash
pip install PySide6 mutagen Pillow requests pypresence python-vlc numpy py7zr
```

Notes:

- `python-vlc` is needed for the VLC playback path.
- `py7zr` is used by the Python updater.
- If a `.7z` package uses unsupported filters, the updater can fall back to an installed **7-Zip** executable.

## Quick start

```bash
python vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed_updater_settings.py
```

You can also pass a file path on launch:

```bash
python vidplayer_2.0.9.1.2_PASSOVER2_portable_vlc_fixed_updater_settings.py "D:\Music\song.mp3"
```

## Project notes

- This README is focused on the current VidPlayer state.
- Full version history is in `CHANGELOG.md`.
