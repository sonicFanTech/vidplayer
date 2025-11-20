Planed updates
--------------
updates for v2.0.9 BETA 4.2

1. Add CD Support [the user will be able to Load any Audio CD within vidplayer, vidplayer will First Check for FFmpeg in the bin Folder, if it's Missing, it'll show some text saying FFmpeg is missing and that it's needed to load/play Audio CDs, if FFmpeg is Found, once the      user selects the CD/DVD Disc Drive where the Audio CD is in, vidplayer then will use FFmpeg to Rip the Data from the Disc to make TEMP Audio Files in a Folder next to the main EXE called "Ripped CDA", the Ripped CDA Folder and TEMP Audio files won't Auto be Deleted just     in case the user wants to Save them and put the Files somewhere else so the user doesn't have to Load/Rip the CD Again]

About VidPlayer
===============
A fast, clean audio player for Windows built with PySide6. VidPlayer focuses on the essentials—playlists, drag-and-drop, double-click to play, and a nostalgic Windows 7-style Aero Glass theme—wrapped in a modern UI. It includes full-screen artwork, rich file info, recent files, and an in-app updater that can download any release asset (EXE/ZIP/7z/etc.) with a progress bar.

Highlights
----------
Windows 7-style Aero Glass theme (with proper enable/disable logic)

Drag & drop files into the main window or playlist

Double-click to play (open files directly when VidPlayer is associated or via command line)

Batch add dialog for large imports (shows each file + progress bar, auto-closes)

Playlist save/load (.vpl / JSON)

Full-screen artwork view with transport controls

File Info panel (length, bitrate, tags, dates, size, location, artwork)

Recent Files menu

Discord Rich Presence (optional)

In-app updater: checks GitHub Releases and can download assets directly with progress

Config & data saved next to the EXE when bundled (PyInstaller-safe)

Supported formats
-----------------
.mp3, .wav, .ogg, .flac, .m4a, .aac, .wma
(Availability of features like precise seeking may vary by format/codec.)

Themes & Settings
-----------------
Themes: Light, Dark, System Default, Aero Glass

“Enable Aero Glass” is only active when the Aero Glass theme is selected

Options: Always on top, Autoplay next, Resume last track/position, Auto-load last playlist, Discord RPC

Install / Run
=============
open CMD [command prompt] and Run the following commad to install the Dependencies [Modules/Packages]

pip install PySide6 pygame mutagen Pillow requests pypresence

you Must have Python 3.13.9 x64 installed on your System 

[if you don't have it, Here's the download Link: https://www.python.org/ftp/python/3.13.9/python-3.13.9-amd64.exe, After it downloads, run the setup wizard, Check the 2 Check Boxes at the bottom of the setup wizard, the Add Python.exe to PATH & use Admin Privileges when installing py.exe, then choose the Customize installation option, Don't uncheck any of the Check boxes, and then click Next, on the next Screen, Check the install Python 3.13 for all users, don't uncheck the 3 Check boxes under that, you can Check the other Check boxes if you so wish to, it's not gonna brake anything]

to Run the .py version of vidplayer.  [.py, the Source code, the non-pre-compiled version] - open CMD [command prompt], and Run the following command.

Python [THE NAME OF THE .PY FILE] [Command EXAMP: Python vidplayer_v2.0.9-BETA4_1.py, you must be in the Directory where the .py file is]

Build Source code
=================
to Build the .py File into a .EXE File, you can use the provided Python compiler Program [Made in Python 3.13.9]

Here's the list of Command to use with the compiler

Commands:
  help, ?                 Show this help text
  list                    Show discovered Python installations
  active                  Show active Python (the Python running this script)
  build <script> [opts]   Build .py -> .exe
      options:
         --python <ver_or_path>   Python identifier (version like 3.8 or a full path to python.exe)
         --arch x86|x64           Target architecture (uses interpreter that matches)
         --icon <path>            Optional icon file (.ico)
         --name <exename>         Output exe name
         -c                       Show pip install output (verbose)
         -BC                      Show build output from PyInstaller
  install_py <version> [x86|x64]   Download & install Python (host must be Windows)
  check_pyinstaller <python>  Check/install PyInstaller for chosen interpreter
  exit, quit              Exit this tool
  run <commandline>       Run a shell command (useful for advanced users)
Examples:
  build myscript.py --python 3.8 --arch x86 --icon C:\icon.ico
  python pybuilder.py build myscript.py --python "C:\Python38-32\python.exe" --arch x86

  Quick start
  ===========
  Open Files… or drag & drop into the main or playlist window
  
  Save/Load Playlist (.vpl/JSON) from the File/Playlist dialogs
  
  Double-click an audio file (if associated) or run VidPlayer.exe "path\to\file.mp3"
  
  View → Full Screen Artwork for an immersive now-playing view
  
  Help → Check for Updates… to open releases or download in-app with a progress bar

  Tech
  ====

  Python + PySide6 (Qt for UI)3
  
  pygame (audio playback), mutagen (tags), Pillow (artwork), requests (updater), pypresence (Discord)

Features / Update / Fixes Log
=============================
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

Fix: updater freeze/crash at 100% (safe thread cleanup), Enhancement: updater can download ANY asset type (no extension filtering), Fix: JSON files now created next to the EXE when compiled (PyInstaller-safe paths), Enhancement: Drag & Drop + multi-open now uses a small progress dialog listing files, adds them one-at-a-time (in a background thread), and auto-closes when finished, First version of vidplayer to have both x64 & x86 versions - v2.0.9 BETA 4.1
