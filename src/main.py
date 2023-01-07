# main.py
#
# Copyright 2023 Altravia
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi
from .WebappManagerWindow import WebAppManagerWindow

gi.require_version("Gtk", "3.0")  # noqa

from gi.repository import Gtk, Gio
from .window import WebappManagerMineWindow


class MyApplication(Gtk.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='it.mijorus.webappmanager',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            wamw = WebAppManagerWindow(application=self)
            win = wamw.window
            self.add_window(win)

        win.present()


def main(version):
    """The application's entry point."""
    app = MyApplication()
    return app.run(sys.argv)
