from time import sleep
import eyes

# Displays a window tracking the specified object, matching a png
# file in /stone_templates. USe this to troubleshoot matching images
eyes.set_debug(True)
eyes.set_display(True)
eyes.set_threshold(0.8)
eyes.match_name("shuriken", 0.5)


# This was used to troubleshoot the application that was stealing
# focus on the MacBook, preventing any cursor clicks.
# https://apple.stackexchange.com/a/170699
# The culprit: /Library/Application Support/Razer/RzDeviceEngine.app
# try:
#     from AppKit import NSWorkspace
# except ImportError:
#     print("Can't import AppKit -- maybe you're running python from brew?")
#     print("Try running with Apple's /usr/bin/python instead.")
#     exit(1)

# from datetime import datetime
# from time import sleep

# last_active_name = None
# while True:
#     active_app = NSWorkspace.sharedWorkspace().activeApplication()
#     if active_app['NSApplicationName'] != last_active_name:
#         last_active_name = active_app['NSApplicationName']
#         # print('%s: %s [%s]') % (
#         #     datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#         #     active_app['NSApplicationName'],
#         #     active_app['NSApplicationPath']
#         # )
#         print(active_app['NSApplicationPath'])
#     sleep(1)
