import pygetwindow as gw
import os
from time import sleep
import subprocess
import time
import pyautogui
import pydirectinput
from PIL import Image
from PIL import ImageGrab


def start_game():
    print('  -Wait for start game')
# Load the target image
    target_image = Image.open(
        os.path.abspath("assets/img/startButton.png"))
    count = 0
    while True:
        screenshot = ImageGrab.grab()  # Take a screenshot of the entire screen
        # Find the target image on the screenshot
        result = pyautogui.locateOnScreen(target_image, confidence=0.60)

        if result is not None:
            # Get the center of the found image
            button_position = pyautogui.center(result)
            print("  -game starting !")
            return True  # Return True after clicking
        else:
            time.sleep(10)  # Wait for a second before checking again
            if count >= 2*60:
                return False
            count += 10


def record():
    screen_width, screen_height = pydirectinput.size()
    # Calculate the center of the screen
    center_x = int(screen_width / 2)
    center_y = int(screen_height / 2)
    # Click on the center of the screen
    pydirectinput.click(center_x, center_y)
    pydirectinput.keyDown('n')
    pydirectinput.keyUp('n')
    sleep(1)
    pydirectinput.keyDown('o')
    pydirectinput.keyUp('o')
    sleep(1)
    pydirectinput.keyDown('u')
    pydirectinput.keyUp('u')
    sleep(1)
    pydirectinput.keyDown('c')
    pydirectinput.keyUp('c')
    sleep(1)
    # zoom out
    # Click on the center of the screen
    pydirectinput.click(center_x, center_y)
    # Press and hold Ctrl+Shift+Z
    pydirectinput.keyDown('ctrl')
    pydirectinput.keyDown('shift')
    pydirectinput.keyDown('z')
    pydirectinput.keyUp('ctrl')
    pydirectinput.keyUp('shift')
    pydirectinput.keyUp('z')
    # Move mouse pointer down 1 times
    pyautogui.scroll(-400)
    # Press and hold Shift+x
    pydirectinput.keyDown('shift')
    pydirectinput.keyDown('x')
    pydirectinput.keyUp('shift')
    pydirectinput.keyUp('x')

    print("Finished")

import keyboard
# Register the hotkey
keyboard.add_hotkey('shift+a', record)

# Keep the program running
keyboard.wait('esc')  # Press 'esc' to exit the programnouc