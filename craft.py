# This assumes that the craft window is available
from time import sleep

import pyautogui
import images as img
import eyes

# Confirm that there are open slots
# Open Menu
# Drag screen to bottom
# Select item crystal option
# Click accept
heart_x, heart_y = img.dim('craft_heart')


def crystals():
    # Open the craft menu, and collect ready items
    craft_point = eyes.match_name('craft_menu')
    counter = 0
    if craft_point:
        img.click(craft_point[0][0], craft_point[0][1], duration=0.3)
        sleep(5)
        for point in eyes.match_name('craft_ready'):
            img.click(point[0], point[1], duration=0.3)
            while True:
                sleep(2)
                ok = eyes.match_name('wide_ok')
                if ok:
                    img.click(ok[0][0], ok[0][1], duration=0.3)
                    break
    while eyes.match_name('craft_start'):
        counter += 1
        start = eyes.match_name('craft_start')[0]
        img.click(start[0], start[1], duration=0.3)
        # Scroll down to bottom menu
        sleep(4)
        for _ in range(3):
            pyautogui.moveTo(300, 700, duration=0.5)
            pyautogui.dragTo(200, 0, duration=0.5)
            sleep(1)
        sleep(3)
        heart = eyes.match_name('craft_heart')
        # Select item crystal
        if counter > 4:
            break
        elif heart:
            img.click(heart[0][0], heart[0][1] - heart_y, duration=0.3)
            sleep(6)
            prompt = eyes.match_name('craft_prompt')
            if prompt:
                img.click(prompt[0][0], prompt[0][1], duration=0.3)
                print("Craft item")
                counter = 0
                sleep(6)
        else:
            print("Something went wrong. Go back to mining")
            break
