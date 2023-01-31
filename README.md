# Webapp Manager - Flatpak port

<p align="center">
  <img width="150" src="https://raw.githubusercontent.com/mijorus/webapp-manager/master/data/icons/hicolor/scalable/apps/it.mijorus.webappmanager.svg">
</p>

Run websites as if they were apps.


## Install

Requirements: `flatpak`, `flatpak-builder`

- Install the required runtime (if needed) `flatpak install org.gnome.Sdk/x86_64/43`
- Run the `install.sh` file

## Status of this fork
This app works, but I'm not interested in publishing it to Flathub just yet.

There is no way at the moment to detect when the user uninstalls a specific browser, which leads to a poor user experience.

Also, I have found some incompatibilities with Epiphany and for this reson it has been removed

If you want to try it yourself because the original app from Linux Mint does not work for you (maybe on fedora or something), please follow the steps described above

## Build

- Download GNOME Builder
- Open this folder with Builder
- Click the hammer icon to compile
- Click the play button to run

## Credits and bug reports
This application is a fork of [Mint's](https://github.com/linuxmint/webapp-manager) original Webapp Manager app; the application was modified in order to run and be distributed on the Flathub store.

The developer of the fork is not affiliated with the Linux Mint team in any way and did not receive any help or approval from the team.

**This app is not ment be a 1-to-1 port and in future releases the two projects might diverge**

Any bug or issue with this app should be reported in this repo.
