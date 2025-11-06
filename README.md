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

About program
=============

VidPlayer — Advanced Audio Player for Windows

Version: v2.0.9 BETA 4.1

VidPlayer is a modern, lightweight, and fully featured audio player built with Python and PySide6.
It combines a clean interface, powerful playlist management, customizable themes (including authentic Windows 7 Aero Glass visuals), and Discord Rich Presence integration — making it both nostalgic and modern.

Features
========

Supports All Common Audio Formats — MP3, WAV, OGG, FLAC, M4A, AAC, WMA, and more.
Windows 7 Aero Glass Theme — Enjoy a sleek, transparent interface inspired by Windows 7’s Aero Glass design.
Playlist Management — Create, save, and load playlists (.vpl or .json) with ease.
Drag & Drop Support — Instantly add files by dragging them into the main or playlist window.
Batch File Loader — When adding many files, a “Loading Files” window appears showing progress, keeping the app stable and responsive.
Auto Resume & Recent Files — Optionally continue playback from where you left off and quickly reopen recent tracks.
Customizable Themes — Choose between Light, Dark, System, or Aero Glass modes.
Full-Screen Artwork Mode — Displays album artwork beautifully, complete with playback controls.
Discord Rich Presence — Show your current song and playback progress on Discord.
Built-in Updater — Automatically checks for new versions and lets you download updates directly through the program with a real progress bar.
Robust Settings Menu — Toggle features like Auto Play Next, Always on Top, Resume Playback, and more.
Comprehensive About Page — Includes Credits, License viewer, and changelog tabs.
Technical Highlights
Built in Python 3 using PySide6 (Qt for Python) for a fast and modern UI.
Uses Pygame for reliable audio playback.
Supports Mutagen for metadata and album art extraction.
Thread-safe architecture for stable background operations (downloads, file loading, etc.).
Safe JSON configuration and playlist saving (auto-created when missing).

