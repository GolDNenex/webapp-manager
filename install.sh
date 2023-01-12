	#! /usr/bin/bash
flatpak kill it.mijorus.webappmanager
flatpak-builder build/ it.mijorus.webappmanager.json --user --install --force-clean
