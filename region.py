import pyautogui as pgui
from time import sleep

if __name__ == '__main__':
    sleep(5)
    position = pgui.position()
    print(position)
