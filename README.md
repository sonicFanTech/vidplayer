Features / Update Log
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

Re-placed the GUI [tkinter] With [pySide6 - Qt], [THE NEW GUI MAY NOT WORK RIGHT ON WINDOWS 10, THE NEW GUI WITH pySide6 WAS MADE FOR WINDOWS 11], Added a New Tool in the Tools Menu called, File info [Shows File metadata like, File Name, File Type / Extension, File Size (MB / KB), File Location (full path), Date & Time of Creation, Artist, Album, Year (if available), Track Length, Bitrate (if available), Copyright (if present in tags), Artwork (embedded or external), If no artwork → text message: “No Artwork Found”], Moved the Full Screen art-work from Tools menu → to the View menu (right below Playlist), Shortcut keys and functionality remain unchanged, Added a New them called Aero Glass, made to look like the Windows 7 Aero Glass them/Effects [this them may get updates to make it look better] - v2.0.9 BETA 1

No update/Fix Log for v2.0.9 BETA 2-3

 Enable Aero checkbox grayed unless theme=Aero (existing), Full Screen Artwork moved to View menu (existing), Re-added update downloader w/ progress (existing), Fixed: Qt stylesheet unsupported props (existing), Fixed: Save/Load QAction triggers (existing) - v2.0.9 BETA 4

Fix: updater freeze/crash at 100% (safe thread cleanup), Enhancement: updater can download ANY asset type (no extension filtering), Fix: JSON files now created next to the EXE when compiled (PyInstaller-safe paths), Enhancement: Drag & Drop + multi-open now uses a small progress dialog listing files, adds them one-at-a-time (in a background thread), and auto-closes when finished - v2.0.9 BETA 4.1
