from __future__ import annotations
from typing import Callable, Any

import os
import pwd
import time
import logging

from newm.layout import Layout
from newm.helper import BacklightManager, WobRunner, PaCtl

from pywm import (
    PYWM_MOD_LOGO,
    PYWM_MOD_ALT
)

pywm = {
    "xkb_options": "grp:win_space_toggle",
    'xkb_layout': "us,ru",
}

logger = logging.getLogger(__name__)

background = {
    'path': os.environ['HOME'] + '/.config/wallpapers/wallpaper.jpg',
    'anim': True
}

outputs = [
    { 'name': 'eDP-1', 'pos_x': 0, 'pos_y': 0, 'width': 1920, 'height': 1080 },
]

wob_runner = WobRunner("wob -a bottom -M 100")
backlight_manager = BacklightManager(anim_time=1., bar_display=wob_runner)
kbdlight_manager = BacklightManager(args="--device='*::kbd_backlight'", anim_time=1., bar_display=wob_runner)
def synchronous_update() -> None:
    backlight_manager.update()
    kbdlight_manager.update()

pactl = PaCtl(0, wob_runner)

def key_bindings(layout: Layout) -> list[tuple[str, Callable[[], Any]]]:
    return [
        ("A-h", lambda: layout.move(-1, 0)),
        ("A-j", lambda: layout.move(0, 1)),
        ("A-k", lambda: layout.move(0, -1)),
        ("A-l", lambda: layout.move(1, 0)),
        ("A-u", lambda: layout.basic_scale(1)),
        ("A-n", lambda: layout.basic_scale(-1)),
        ("A-t", lambda: layout.move_in_stack(1)),

        ("A-H", lambda: layout.move_focused_view(-1, 0)),
        ("A-J", lambda: layout.move_focused_view(0, 1)),
        ("A-K", lambda: layout.move_focused_view(0, -1)),
        ("A-L", lambda: layout.move_focused_view(1, 0)),

        ("A-C-h", lambda: layout.resize_focused_view(-1, 0)),
        ("A-C-j", lambda: layout.resize_focused_view(0, 1)),
        ("A-C-k", lambda: layout.resize_focused_view(0, -1)),
        ("A-C-l", lambda: layout.resize_focused_view(1, 0)),

        ("A-Return", lambda: os.system("kitty &")),
        ("A-d", lambda: os.system("dmenu_path | wofi --show drun --prompt=application -I | newm-cmd launcher -- &")),

        ("A-q", lambda: layout.close_focused_view()),

        ("A-p", lambda: layout.ensure_locked(dim=True)),
        ("A-P", lambda: layout.terminate()),
        ("A-C", lambda: layout.update_config()),

        ("A-f", lambda: layout.toggle_fullscreen()),

        ("A-", lambda: layout.toggle_overview()),

        ("XF86MonBrightnessUp", lambda: backlight_manager.set(backlight_manager.get() + 0.1)),
        ("XF86MonBrightnessDown", lambda: backlight_manager.set(backlight_manager.get() - 0.1)),
        ("XF86KbdBrightnessUp", lambda: kbdlight_manager.set(kbdlight_manager.get() + 0.1)),
        ("XF86KbdBrightnessDown", lambda: kbdlight_manager.set(kbdlight_manager.get() - 0.1)),
        ("XF86AudioRaiseVolume", lambda: pactl.volume_adj(5)),
        ("XF86AudioLowerVolume", lambda: pactl.volume_adj(-5)),
        ("XF86AudioMute", lambda: pactl.mute()),
    ]

panels = {
    'lock': {
        'cmd': 'alacritty -e newm-panel-basic lock',
    },
    'launcher': {
        'cmd': 'alacritty -e newm-panel-basic launcher'
    },
    'top_bar': {
        'native': {
            'enabled': True,
            'texts': lambda: [
                pwd.getpwuid(os.getuid())[0],
                time.strftime("%c"),
            ],
        }
    },
}

energy = {
    'idle_callback': backlight_manager.callback
}
