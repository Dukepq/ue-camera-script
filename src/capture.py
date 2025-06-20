import time
import os
import json
import pyscreeze
from utils import build_rotate_command, mk_dynamic_folder, get_dirname
from pynput import keyboard as _keyboard
from input import controller_id
import pyperclip

__dirname = get_dirname()

keyboard = _keyboard.Controller()
Key = _keyboard.Key

def rotate_to(theta, phi):
  rotate_cmd = build_rotate_command(phi, theta, controller_id)
  pyperclip.copy(rotate_cmd)
  keyboard.tap("$")
  time.sleep(0.1)

  keyboard.press(Key.ctrl)
  keyboard.press("v")
  keyboard.release(Key.ctrl)
  keyboard.release("v")

  time.sleep(0.1)
  keyboard.tap(Key.enter)


def capture_tiles():
    filePath = os.path.join(__dirname, "..", "static",  "points.json")
    file = open(filePath, "r")
    points = json.load(file)

    folder_out_path = mk_dynamic_folder()

    count = 0
    for point in points:
      rotate_to(point["theta"], point["phi"])
      time.sleep(0.3)

      file_path = os.path.join(folder_out_path, f"{count}-{point["theta"]}_{point["phi"]}.png")
      pyscreeze.screenshot(file_path)
      print(f"captured: {count}_{point["theta"]}_{point["phi"]}.png")
      count += 1
