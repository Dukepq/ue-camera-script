import time
import os
import json
import pyscreeze
from utils import build_rotate_command, mk_dynamic_folder, get_dirname
from pynput import keyboard as _keyboard
import constants as c
import pyperclip

__dirname = get_dirname()

keyboard = _keyboard.Controller()
Key = _keyboard.Key

def rotate_to(theta, phi):
  rotate_cmd = build_rotate_command(phi, theta, c.controller_id)
  pyperclip.copy(rotate_cmd)
  keyboard.tap(c.toggle_console_key)
  time.sleep(c.wait_time_s)

  keyboard.press(Key.ctrl)
  keyboard.press("v")
  keyboard.release(Key.ctrl)
  keyboard.release("v")

  keyboard.tap(Key.enter)


def capture_tiles():
    filePath = os.path.join(__dirname, "..", "static",  "points.json")
    file = open(filePath, "r")
    points = json.load(file)

    folder_out_path = mk_dynamic_folder(c.game_title or "notitle")

    count = 0
    for point in points:
      rotate_to(point["theta"], point["phi"])
      time.sleep(c.wait_time_s * 3)

      filename = f"idx={count}_theta={point["theta"]}_phi={point["phi"]}.png"
      file_path = os.path.join(folder_out_path, filename)
      pyscreeze.screenshot(file_path)
      print(f"captured: {filename}")
      count += 1
