import cv2 as cv
import numpy as np
import pyautogui

screenWidth, screenHeight = pyautogui.size()
# Order is important. Room gear dependent on expand. Errors full priority
singles = "ad_x reward error daily_ok wide_ok expand room_gear".split()
stones = ("clover four_clover hadouken donut "
          "bronze silver gold "
          "crescent half_moon full_moon "
          "snowball ice_cube ").split()


def click(x, y, duration=0.3):
    pyautogui.moveTo(x, y, duration)
    pyautogui.dragTo(x + 1, y + 1)


def screenshot(x0=0, y0=0, x1=screenWidth / 2, y1=screenHeight):
    _img = pyautogui.screenshot(region=(x0, y0, x1, y1))
    return cv.cvtColor(np.array(_img), cv.COLOR_RGB2BGR)


def info(t):
    img = cv.imread('stone_templates/{}.png'.format(t))
    return t, img


def dim(t):
    img = cv.imread('stone_templates/{}.png'.format(t))
    return img.shape[1], img.shape[0]


def single_templates():
    return [info(t) for t in singles]


def templates(match_crescent=True):
    template_names = singles + stones
    if not match_crescent:
        template_names.remove('crescent')
    return [info(t) for t in template_names]


def pouch():
    return info('pouch')
