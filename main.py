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

        # (25, 179, 25) GREEN HEALTH BAR
        # (25, 255, 255) YELLOW HEALTH BAR
        # (0, 0, 255) RED HEALTH BAR

        if (b, g, r) in [
            (25, 179, 25),
            (25, 255, 255),
            (0, 0, 255)
        ]:
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
        
        # If loot chest, open and take items

        pyautogui.press('shift')
        time.sleep(0.5)

        # Click at (1135, 559) -> BGR = (101, 171, 204)
        monitor_loot = {
            "left": 1135,
            "top": 559,
            "width": 1,
            "height": 1
        }

        img_loot = np.array(sct.grab(monitor_loot))
        b, g, r, a = img_loot[0, 0]

        if b == 101 and g == 171 and r == 204:
            
            # Click Take All
            pyautogui.moveTo(1054, 843)
            pyautogui.click()
            time.sleep(2)
            pyautogui.click()
            
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