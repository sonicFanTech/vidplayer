# VidPlayer Changelog

A detailed running log of VidPlayer changes across builds.

---

## v2.0.9.3.1.1 Beta X64

### Version / build status
- Version string updated to `v2.0.9.3.1.1 Beta X64`
- This build moves VidPlayer forward from the unreleased Experimental branch into a Beta build
- This Beta focuses mainly on:
  - Multi-language support
  - VPTheme engine integration in VidPlayer
  - UI sound support
  - Appearance / theme workflow improvements
  - Playlist / settings / updater polish
- Continues the portable VLC-based VidPlayer branch
- Continues the external updater workflow

### Multi-language support
- Added multi-language UI support to VidPlayer
- Added `.langu` language file support
- `.langu` files use a JSON-based structure
- Added UI language file loading from `bin\\Langu\\UI\\`
- Added localized docs loading from `bin\\Langu\\Docs\\`
- Added a language selector in Settings
- Added reload language files support in Settings
- Added fallback handling for missing language files
- Added fallback handling for missing localized docs
- Improved language scanning and language listing logic

### VPTheme engine integration
- Added the newer VPTheme system into VidPlayer
- Added `.vptheme` loading from `bin\\VPThemes\\`
- Added theme selection support in Settings
- Added reload VPThemes support in Settings
- Added open VPThemes folder support in Settings
- Added config-backed theme selection persistence
- Added support for built-in Light / Dark / System Default theme handling through the newer theme workflow

### Theme engine support now used in VidPlayer
- Added support for themed main window colors
- Added support for themed dialog colors
- Added support for themed menubar colors
- Added support for themed input colors
- Added support for themed tab colors
- Added support for themed playlist colors
- Added support for themed tooltip colors
- Added support for themed group box title colors
- Added support for themed slider colors
- Added support for themed progress bar colors
- Added support for theme gradients in supported areas
- Added support for theme-controlled fonts
- Added support for theme-controlled icons
- Added support for theme-controlled UI sounds

### Theme asset support
- Added theme asset loading support for:
  - sounds
  - icons
  - fonts
- Added support for built-in default UI sounds from `bin\\VPThemes\\Default\\Sounds\\`
- Added support for packaged custom theme folders such as:
  - `VPThemes\\ThemeName\\Theme.vptheme`
  - `VPThemes\\ThemeName\\Sounds\\`
  - `VPThemes\\ThemeName\\Icons\\`
  - `VPThemes\\ThemeName\\Fonts\\`
- Added support for `Default/...` asset paths
- Added support for relative per-theme asset paths
- Added font fallback handling when a requested theme font cannot be loaded
- Themes remain usable even if a requested custom font fails and VidPlayer has to fall back to default fonts

### Theme icon support
- Added theme icon override support for:
  - app / artwork placeholder logo
  - Play
  - Pause
  - Stop
  - Previous
  - Next
- Theme icon overrides now apply to the real main playback controls
- Theme logo overrides can be used in the small artwork / logo display area
- Fallback icon behavior still remains when a theme icon is missing

### UI sound support
- Added UI sound support to VidPlayer
- Added enable / disable UI sounds setting
- Added enable / disable UI hover sounds setting
- Added UI sound volume control
- Added support for default built-in UI sounds for built-in themes
- Added support for custom UI sound packs in custom themes

### UI sound event support
- Added general button click sound support
- Added general hover sound support
- Added dialog open sound support
- Added dialog close sound support
- Added confirm / success sound support
- Added error sound support
- Added tab-switch sound support
- Added playback control sound support for:
  - Play
  - Pause
  - Stop
  - Previous
  - Next
- Added top menubar sound support for:
  - File
  - View
  - Tools
  - Help
- Added menu item hover / click sound groundwork and support
- Improved playback control sound fallback behavior when a theme-specific control sound is missing

### Settings / appearance workflow
- Reworked the Settings workflow for the newer theme / appearance system
- Added a dedicated Appearance area / tab workflow for:
  - theme selection
  - VPTheme controls
  - UI sound controls
  - UI sound volume
- Moved appearance-related controls into a more focused workflow
- Theme reload / theme-folder actions are easier to access from Settings

### Playlist / loading workflow
- Improved loading behavior for large batches of audio files
- Large file-add / playlist-load operations now use the loading / adding progress workflow more consistently
- Added Unload Playlist support
- Added Clear Playlist support
- Improved playlist handling so manually added items and loaded playlist content can be managed more cleanly

### Subtitle / lyrics systems
- Subtitle / lyrics support from the unreleased Experimental branch remains part of this Beta
- Subtitle / lyrics settings continue to be available in Settings
- Subtitle / lyric appearance settings now fit better into the newer Settings / theme workflow

### Updater / rollback / settings integration
- Updater settings remain integrated into VidPlayer
- Continued support for:
  - startup update checking
  - channel selection
  - silent mode
  - rollback limit settings
  - auto-open / auto-close updater behaviors
- Rollback manager access remains available from Settings
- Improved integration between VidPlayer settings and updater behavior

### General bug fixes / polish
- Fixed the long-standing Pause button issue where Stop → Play could leave Pause not working correctly
- Improved theme application reliability across more windows and controls
- Improved updater-page theming behavior in Settings
- Improved About window theming / text readability in themed builds
- Improved custom icon runtime application
- Improved menu / control sound triggering behavior
- Improved theme asset fallback behavior
- Improved startup handling around the newer theme / asset systems
- General UI / settings / playback polish from the unreleased Experimental branch continues in this Beta

### Beta notes
- This is the first public build after the unreleased Experimental branch
- The VPTheme system is now a major built-in part of VidPlayer itself
- Multi-language support is now built into the player
- This is not intended to be the final full Release build
- More translation work, testing, and polish are still expected after this Beta

---

## v2.0.9.3 Release X64

### Version / app info
- Version string updated to `v2.0.9.3 Release X64`
- Continues the portable VLC-based VidPlayer branch
- Continues the external updater workflow
- This release mainly focuses on a major UI / artwork / icon / File Info refresh

### Main UI / icon refresh
- Added custom `.ico`-based UI icon support across the player
- VidPlayer now loads custom icons from:
  - `bin\\icons\\buttons\\`
  - `bin\\icons\\menubar\\`
  - `bin\\icons\\VPLogo.ico`
- Main playback controls now use the custom icon set
- Menu bar actions now use custom icons for supported actions
- Added VPLogo placeholder support into the main player UI
- Built-in fallback transport icons used in the older updated areas were replaced by the new custom icon workflow

### Full Screen Artwork
- Reworked Full Screen Artwork mode to behave more like a true full-screen takeover view
- Full-screen artwork controls now use the custom button icon set
- Full-screen artwork now updates automatically when the current track changes
- Full-screen artwork now refreshes the shown artwork instead of only keeping the image from when the window first opened
- Full-screen artwork now shows `VPLogo.ico` when the current track has no embedded artwork
- Full-screen placeholder behavior now better matches the main window artwork display

### File Info window
- Reworked the built-in File Info window using logic based on the EveryPlay-style MediaInfo tool workflow
- Added deeper `ffprobe`-based media inspection support
- Added a more detailed multi-tab File Info layout
- Added a Basic info tab with expanded media / container / stream details
- Added a Codecs tab for stream / codec information
- Added an Extra / Raw tab for raw probe-style information
- Added better artwork handling in the File Info window
- Added support for showing a loaded-file list in File Info when more than one track is loaded in VidPlayer

---

## v2.0.9.1.2 Pre-Release X64
- Python-based external updater rework
- Shared updater settings file
- Rollback snapshots with manifests
- Mini Mode and playlist docking polish
- Portable VLC DLLs updated to 3.0.23

---

## v2.0.9.1.1 Experimental
- Dockable playlist mode added
- Playlist can dock to top, right, left, bottom, or with the visualizer as a tab
- Mini Mode introduced

---

## v2.0.9.1 Pre-Release
- Built-in updater removed
- External updater branch started
- VLC-based playback branch continued
- Subtitle / lyrics support added

---

## v2.0.9 Release
- Added playlist search box
- Added FFT-based visualizer under the main timeline
- Fixed autoplay-next behavior
- Aero Glass removed for stability improvements
