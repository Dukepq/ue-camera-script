from pynput import keyboard
import events

with keyboard.Listener(
   on_press = events.on_press,
) as listener:
   print("Waiting for input... (f10 to exit program)")
   listener.join()
