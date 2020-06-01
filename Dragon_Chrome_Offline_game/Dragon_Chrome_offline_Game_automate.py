import pyautogui as pag
from PIL import Image, ImageGrab
import time

def hit(key):
    pag.keyDown(key)
    return

# def takeScreenshot():
#     image = ImageGrab.grab().convert('L')    # to convert to greyscale
#     return image

def isCollide(data):
    # draw the rectangle for bird
    # for i in range(340, 390):
    #     for j in range(410, 553):
    #         if data[i, j] < 85:
    #             hit('down')
    #             return

    # draw the rectangle for cactus
    for i in range(280, 520):
        for j in range(553, 660):
            if data[i, j] < 85:  # check if there is any grey pixel
                hit('up')
                return
    return

if __name__ == '__main__':
    print('Hey Dino game about to start in 3 seconds')
    time.sleep(3)
    hit('up')          # this up key hit is to begin the game
    while(True):
        image = ImageGrab.grab().convert('L')    # to convert to greyscale
        data = image.load()
        isCollide(data)
        #image.show()
        # # draw the rectangle for bird
        # for i in range(340, 390):
        #     for j in range(410, 553):
        #         data[i,j] = 127
        #
        # # draw the rectangle for cactus
        # for i in range(280, 520):
        #     for j in range(553, 660):
        #         data[i, j] = 0
        # image.show()
        # break