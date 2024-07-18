#!/usr/bin/python3
import subprocess
import json
import time

while True:
    devices = subprocess.run("hyprctl -j devices", shell=True, capture_output=True).stdout.decode()
    devices_dict = json.loads(devices)

    main_keyboard = [kb for kb in devices_dict["keyboards"] if kb["main"] == True][0]
# dict = {
#     "text": main_keyboard["active_keymap"],
# }

    print(main_keyboard["active_keymap"])
    time.sleep(0.1)
