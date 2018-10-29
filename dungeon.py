# This assumes that the craft window is available
from time import sleep
import eyes
import images as img


# This function supports automatically replaying mine
# dungeons, attempting to re-enter the dungeon.
# It will only attempt to enter when detecting the prompt.
# Three failed attempts at entering (spaced by 10 seconds)
# will assume that no more entry tickets are available, and
# the mine_return button will be clicked. This function is best
# used before the main matching logic, to smoothly return matching
def mine():
    while True:
        mine_replay = eyes.match_name('mine_replay')
        if not mine_replay:
            sleep(10)
        else:
            for _ in range(3):
                if eyes.match_name('mine_replay'):
                    img.click(mine_replay[0][0], mine_replay[0][1], duration=0.3)
                    sleep(10)
                else:
                    break
            mine_return = eyes.match_name('mine_return')
            if mine_return:
                img.click(mine_return[0][0], mine_return[0][1], duration=0.3)
                break


# Automatically enter TOC until no more tickets are available.
# This assumes that you are already at the TOC screen, as
# the function is dependent on the yellow play icon
def toc():
    while True:
        prompt = eyes.match_name('toc')
        if not prompt:
            sleep(15)
        else:
            img.click(prompt[0][0], prompt[0][1], duration=0.3)
            sleep(10)
            # Try three more times. If still detected, go back to mine (out of tickets)
            for _ in range(3):
                prompt = eyes.match_name('toc')
                if prompt:
                    print('Reattempt TOC')
                    img.click(prompt[0][0], prompt[0][1], duration=0.3)
                    sleep(8)
                else:
                    break
            if eyes.match_name('toc'):
                print('Return to mine')
                mine_return = eyes.match_name('mine')
                img.click(mine_return[0][0], mine_return[0][1], duration=0.3)
