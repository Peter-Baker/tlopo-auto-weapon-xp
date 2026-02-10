import mss
import numpy as np
import time
import threading
import pyautogui
from pynput import keyboard

running = False
stop_program = False

def check_enemy_exists():

    with mss.mss() as sct:

        # -------- Check if enemy exists ---------
        """

        monitor_left = {
            "left": 1390,
            "top": 199,
            "width": 1,
            "height": 1
        }

        img = np.array(sct.grab(monitor_left))
        b, g, r, a = img[0, 0]

        if b == 254 and g == 254 and r == 254:
            print ("Restarting Game...")
            pyautogui.click(1293, 1095) # Click Brew Again
            time.sleep(0.5)
            pyautogui.click(1685, 910) # Click OK to maxed out potions
            time.sleep(0.5)
        
        """
        
        # -------- Attack --------

        



def worker():
    global running, stop_program

    while not stop_program:
        if running:
            check_enemy_exists()
            time.sleep(1)
        else:
            time.sleep(0.1)

def on_press(key):
    global running, stop_program

    # toggle with any key
    if key == keyboard.Key.esc:
        print("Exiting...")
        stop_program = True
        return False

    running = not running

    if running:
        print("Started checking every 2 seconds...")
    else:
        print("Stopped checking.")

print("Press any key to start / stop checking.")
print("Press ESC to exit.")

t = threading.Thread(target=worker, daemon=True)
t.start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# PRESS ESC TO END PROGRAM