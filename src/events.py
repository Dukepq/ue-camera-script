from pynput import keyboard
from capture import capture_tiles
import sys
import threading

c_thread = None

def run_capture():
  print("Taking mouse control and capturing images...")
  capture_tiles()
  print("Finished capturing images.")

def on_press(key):
  global c_thread
  if key == keyboard.Key.f2:
    if not c_thread or not c_thread.is_alive():
      c_thread = threading.Thread(target=run_capture)
      c_thread.start()
    else:
      print("Already capturing images...")
  if key == keyboard.Key.f10:
     print("Terminating...")
     sys.exit()
