from pynput import keyboard
import events
import constants as c

if (c.controller_id == None):
  c.controller_id = input("Controller id: ")

with keyboard.Listener(
   on_press = events.on_press,
) as listener:
   print("f2 to start capturing... (esc to exit program)")
   listener.join()
