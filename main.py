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

        # Health Bar Green: Click at (1143, 189) -> BGR = (25, 179, 25)

        monitor_healthbar = {
            "left": 1143,
            "top": 189,
            "width": 1,
            "height": 1
        }

        img = np.array(sct.grab(monitor_healthbar))
        b, g, r, a = img[0, 0]

        if b == 25 and g == 179 and r == 25:
            # -------- Attack --------
            pyautogui.press('ctrl')
            time.sleep(0.5)
            pyautogui.press('ctrl')
            time.sleep(0.5)
            pyautogui.press('ctrl')
            time.sleep(1)
            pyautogui.press('ctrl')
            time.sleep(1)
            pyautogui.press('ctrl')
            time.sleep(1)
            
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
    
    if key == keyboard.Key.f7:
        
        running = not running

        if running:
            print("Started checking every 2 seconds...")
        else:
            print("Stopped checking.")

print("Press F7 to start / stop checking.")
print("Press ESC to exit.")

t = threading.Thread(target=worker, daemon=True)
t.start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# PRESS ESC TO END PROGRAM