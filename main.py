from time import sleep
import time
import pyautogui
import eyes
import images as img
import craft
import dungeon

debug = False
display = True
threshold = 0.80
eyes.set_debug(debug)
eyes.set_display(display)
eyes.set_threshold(threshold)
templates = img.templates(match_crescent=True)
screenWidth, screenHeight = pyautogui.size()
actions = 0
# Set start_time to time.time() if you do not want to start crafting right away
start_time = 0
crystal_time = 0
crystal_limit = 15 * 60

try:
    # Go to dungeon.py to get more information
    # dungeon.mine()
    # dungeon.toc()
    while True:
        did_match = False
        source = img.screenshot()
        for tname, timg in templates:
            matching_points = eyes.match(tname, timg, source, threshold)
            if matching_points:
                # Expand bag for full inventory. Gear is hidden upon opening
                if tname == 'ruby':
                    # Click pouch to expand
                    pouch = img.info('pouch')
                    pouch_point = eyes.match(pouch[0], pouch[1],
                                             source)
                    if pouch_point: 
                        img.click(
                            pouch_point[0][0],
                            pouch_point[0][1],
                            duration=0.3)
                        actions += 1
                        did_match = True
                    break
                # Close occasional menu pop-ups
                elif tname in img.singles:
                    img.click(
                        matching_points[0][0],
                        matching_points[0][1],
                        duration=0.3)
                    actions += 1
                    did_match = True
                    break
                # Always hold three crescents, for crafting
                elif (time.time() - crystal_time) > crystal_limit:
                    crystal_time = time.time()
                    craft.crystals()
                elif tname == 'crescent' and len(matching_points) < 5:
                    pass
                elif len(matching_points) >= 2:
                    pyautogui.moveTo(
                        matching_points[0][0],
                        matching_points[0][1],
                        duration=0.3)
                    pyautogui.dragTo(
                        matching_points[1][0],
                        matching_points[1][1],
                        duration=0.5)
                    if debug:
                        print('Dragging from {} to {}'.format(
                            (matching_points[0][0], matching_points[0][1]),
                            (matching_points[1][0], matching_points[1][1])))
                    actions += 1
                    did_match = True
                    sleep(1)
                    # break
        if did_match:
            sleep(0.5)
        else:
            if debug:
                print('No match found')
            pyautogui.moveTo(screenWidth/4, 0, duration=0.3)
            pyautogui.moveTo(screenWidth/4, screenHeight/8, duration=8)

except KeyboardInterrupt:
    pass

e = time.time() - start_time
elapsed_time = "{:.0f}:{:.0f}:{:.0f}".format(e/3600, (e%3600)/60, (e%60))
print('Program finished after performing {} actions over {}'.format(actions, elapsed_time))
