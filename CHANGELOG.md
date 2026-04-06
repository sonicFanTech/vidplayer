# VidPlayer Changelog

This file tracks VidPlayer changes across builds, including features, fixes, removals, UI changes, playback changes, and updater changes.

---

## v2.0.9.1.2 Pre-Release X64

### Version / app info

- Version changed to `v2.0.9.1.2 Pre-Release X64`
- Updated Discord App ID

### UI / Mini Mode

- Reworked Mini Mode UI styling to look cleaner and more modern
- Improved Mini Mode artwork scaling so artwork no longer stretches badly in unusual window sizes
- Reworked Mini Mode background layering / artwork presentation
- Improved Mini Mode controls styling and layout
- Improved Mini Mode button sizing / spacing
- Improved Mini Mode overlay look
- Improved Mini Mode seek bar styling
- Improved Mini Mode margins / spacing
- Improved Mini Mode menu reveal / restore behavior
- Added / documented F10 help for revealing the menu bar again in Mini Mode
- Prevented maximize behavior while Mini Mode is enabled
- Fixed Mini Mode window restore sizing when leaving Mini Mode
- Fixed Mini Mode background updates on resize
- Fixed subtitle / lyrics visibility issues in Mini Mode
- Mini Mode now force-hides subtitle / lyrics labels at runtime
- Subtitle auto-load / refresh no longer makes subtitle / lyrics labels reappear in Mini Mode

### Playlist / docking

- Improved docked playlist polish and stability
- Dock location menu items are now checkable
- Current dock location stays visibly selected
- Status bar / state updates are cleaner when docking changes
- Fixed playlist refresh bug / recursive refresh issue
- Dock With Visualizer becomes unavailable when the visualizer is disabled
- Previous Dock With Visualizer selections no longer wrongly force the visualizer area to appear when the visualizer is disabled

### Visualizer

- Reworked experimental live VLC data visualizer handling
- Analyzer player now recreates itself per track
- Live VLC analyzer reset / watchdog behavior is cleaner
- Reduced cases where Live VLC data disables itself when switching tracks
- General experimental live VLC data behavior improved

### VLC loading window

- Updated the VLC loading window to show more startup details
- Still lists core DLL loading
- Now also lists extra DLL files found in `VLCLibs`
- Now also lists VLC plugin DLLs found in the plugins folder
- Improved startup detail logging for VLC troubleshooting

### Audio CD playback changes in VidPlayer

- Removed the old **Use VLC for Audio CD playback** setting
- Audio CD playback now goes through the main VidPlayer window / main playback flow
- Removed the old built-in rip-first Audio CD playback path
- Audio CD now uses the drive the user selected instead of assuming one drive letter
- Audio CD tracks can now appear in the playlist even though they are not normal audio files
- Audio CD playlist entries can now be played through the main playback flow
- Removed the built-in Audio CD ripping path in favor of an external ripper workflow

### External Audio CD ripper tool

- Added support for launching an external Audio CD ripper tool from the Tools menu
- VidPlayer now looks for the external ripper in `bin\`
- Preferred ripper file name: `VPACDRipper.exe`
- Fallback file names can still be supported for compatibility
- Fixed a bug where VidPlayer failed to open the Audio CD ripper even when it existed in `bin\`
- External ripper launch now uses a better working directory / launch path

### External updater rework

- Reworked the updater into a Python-based external updater flow
- Added safer partial update logic instead of broad replace-everything behavior
- Added checksum / manifest-based compare logic
- Added real rollback snapshots that store only files that changed during an update
- Rollback now restores changed files and removes files that were added by the updated build
- Updater now skips protected content such as the `update\` folder itself
- Updater now skips updater files so it does not try to replace itself while running
- Updater now skips common uninstaller files in the install root
- Updater keeps JSON / user data files local by default instead of overwriting them from the package
- Added fallback extraction behavior for `.7z` packages that `py7zr` cannot fully extract
- Updater can fall back to a system `7z.exe` / `7za` / `7zr` installation when needed
- Improved updater progress / stage display
- Added shared updater settings file support through `update\updater_settings.json`
- Added VidPlayer settings integration for updater settings
- Added updater settings for:
  - auto-check enabled
  - check every N launches
  - auto-open VidPlayer after update / rollback
  - close VidPlayer when launching updater
- VidPlayer launcher logic now respects shared updater settings
- VidPlayer can launch either `VidPlayerUpdater.exe` or `VidPlayerUpdater.py`

### General fixes / changes

- Updated handling for display names in playlist entries
- General polish to Mini Mode, playlist docking, updater flow, and Audio CD support
- Multiple UI / workflow bug fixes from experimental builds

---

## v2.0.9.1.1 Experimental

### Experimental / UI work

- Added new setting: **Enable Dockable Playlist Mode**
- Playlist can now dock into the main window in 5 spots:
  1. Top
  2. Right
  3. Left
  4. Bottom
  5. With the visualizer as a tab
- Docked playlist can undock itself when Dockable Playlist Mode is disabled
- Added Mini Mode in the View menu
- Added `Ctrl+M` shortcut for Mini Mode
- In Mini Mode:
  - the window becomes much smaller but is still resizable
  - artwork becomes the background / main focus
  - main controls become icon-style mini controls
  - menu bar can auto-hide
  - some settings become disabled / grayed out
  - Dockable Playlist Mode is disabled while in Mini Mode
  - subtitle / lyrics settings are disabled while in Mini Mode
- Added View menu options for dock playlist placement
- Fixed `Ctrl+L` behavior so it opens Playlist instead of loading a playlist
- Added first pass of Mini Mode background / layout / artwork scaling work
- Added first pass of playlist docking UI and visualizer-tab docking mode

---

## v2.0.9.1 Pre-Release

### Major changes

- Removed the built-in updater
- Replaced it with an external updater workflow

### External updater

- Original external updater build was made in C++
- Added full custom updater window / UI / title bar
- Added SHA-256 hash matching for local and online files
- Added checksum system
- Added rollback support
- Added auto-close / auto-open VidPlayer behavior after update

### VidPlayer changes

- Added launch-counter-based external updater auto-run behavior
- Added subtitle / lyrics support
- Added subtitle / lyrics settings

### Subtitle / lyrics settings

- Enable subtitle / lyrics display
- Auto-load sidecar subtitle file with the same audio filename
- Font size
- Bold text
- Font color with HEX input / picker
- Background on / off
- Background color picker
- Background opacity
- Display position options
- Timing offset
- Manual subtitle file loading

### Playback changes

- Playback path moved to a fully VLC-based direction for newer builds

---

## v2.0.9 Release

### Added

- Playlist search box
- Playlist filtering by filename while typing
- FFT-based visualizer under the main timeline
- Visualizer settings for enable / disable, FPS, size, and color

### Fixed

- Fixed auto-play next file in playlist behavior so it correctly advances when enabled

### Removed

- Removed the experimental Aero Glass theme / effect to improve stability and simplify theming

---

## v2.0.9 BETA 4.2

### Audio CD support

- Added **File → Play Audio CD…**
- Added **Playlist → Play Audio CD…** button
- Implemented Audio CD ripping using `cdda2wav` (preferred) or `cdparanoia`
- Ripped tracks into a timestamped session folder and then into a shared `Ripped CDA` folder
- Added output format options:
  - WAV
  - MP3
  - OGG
  - FLAC
- Used `ffmpeg` for transcoding when compressed formats were chosen
- Added ripping / conversion progress dialogs
- Added option to add ripped tracks to the current playlist
- Cleaned up temporary `.inf` files created by `cdda2wav`

### Experimental VLC Audio CD playback

- Added optional VLC-based Audio CD playback
- Added **Use VLC for Audio CD playback (experimental)** setting
- When enabled, **Play Audio CD…** opened a small VLC-backed CD player window
- Used local VLC DLLs from `bin/VLCLibs` with `python-vlc`

### Notes

- First build that was no longer treated as a BETA build in the older README notes

---

## v2.0.9 BETA 4.1

### Updater / build / import work

- Fixed updater freeze / crash at 100%
- Updater could now download any asset type from GitHub releases
- JSON files such as `config.json`, `recents.json`, and `artmap.json` were created next to the EXE for bundled builds
- Drag & drop / multi-open gained a background-threaded progress dialog
- Batch add dialog listed each file being added and auto-closed when complete
- First VidPlayer release to ship both x64 and x86 builds

---

## v2.0.9 BETA 4

### UI / stability

- Correctly disabled the **Enable Aero Glass** checkbox unless the Aero theme was selected
- Confirmed Full Screen Artwork under the View menu
- Re-added update downloader with progress dialog
- Fixed crashes caused by unsupported Qt stylesheet properties
- Fixed Save / Load `QAction` triggers

---

## v2.0.9 BETA 2–3

- No public update / fix log recorded for these builds

---

## v2.0.9 BETA 1

### Major UI rework

- Replaced the older Tkinter GUI with a PySide6 / Qt GUI
- Added a File Info tool under the Tools menu
- File Info showed:
  - file name
  - file type / extension
  - size
  - path
  - creation / modification timestamps
  - artist / album / year
  - track length / bitrate
  - copyright tag
  - embedded or external artwork preview
- Added a new Aero Glass theme inspired by Windows 7 Aero effects
- Moved Full Screen Artwork from Tools to View

---

## v2.0.8.1

- External artwork paths were persisted in `artmap.json`
- External artwork could be restored across restarts
- Added previous / next buttons in the fullscreen overlay
- Overlay auto-hid after inactivity and reappeared on mouse move
- Improved persistence of manually chosen external artwork

---

## v2.0.8

- Added Discord Rich Presence toggle in Settings
- App maintained a single RPC connection shared with the playlist window
- Added **Always on top** setting
- Added fullscreen artwork entry / workflow
- Escape exited fullscreen
- Clicking artwork toggled play / pause
- Added filename label and close button in fullscreen view
- Saved new settings to `config.json` and loaded them at startup

---

## v2.0.7

- Added Discord Rich Presence integration
- Changed default volume to `50.0`

---

## v2.0.6.1

- Updated License Agreement
- License and Features / Update Log tabs began loading text from external files instead of hard-coded text
- Added auto-check for updates on startup
- Added **Check for updates** button to the About menu

---

## v2.0.6

- Added a new About window

---

## v2.0.5

- Added a progress / loading window when opening more than 10 files

---

## v2.0.4

- Fixed auto-play next track behavior
- Added more options to the Settings window

---

## v2.0.3

- First attempt at auto-play next file in playlist
- Build was broken and never publicly released

---

## v2.0.2

- Added embedded artwork display
- Added Settings window
- Reworked volume slider, though it was temporarily broken in that stage
- Added playlist support

---

## v2.0.1

- Player UI redesigned again
- Added Light / Dark mode
- Added Recent Files list

---

## v2.0.0

- Program rewritten for Python 3.12+
- Major internal rework of the player
