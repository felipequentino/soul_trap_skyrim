# The key that you want to press to stop the script (default is 'x')
STOP_KEY = 'x'

# The number of casts you want to do before restart the loop by waiting 
CASTS_BEFORE_WAIT = 2

from pywinauto import  keyboard, mouse
from keyboard import  wait
from threading import Thread
import pygetwindow as gw
import time

is_pressed = False

def update_steps():
    global is_pressed

    wins = gw.getWindowsWithTitle('Skyrim Special Edition')
    print(wins)
    win = wins[0]
    win.activate()
    time.sleep(4)    
    keyboard.send_keys('{ESC}')
    
    while not is_pressed:
        time.sleep(0.5)
        
        for i in range(CASTS_BEFORE_WAIT):
            mouse.press(button='left', coords=(0, 0))
            mouse.press(button='right', coords=(0, 0))
            time.sleep(1)
            mouse.release(button='left', coords=(0, 0))
            mouse.release(button='right', coords=(0, 0))
        
        time.sleep(0.5)
        keyboard.send_keys('{t down}')
        keyboard.send_keys('{t up}')
        time.sleep(0.5)
        keyboard.send_keys('{ENTER}')


def event_listener():
    global is_pressed
    wait(STOP_KEY)
    is_pressed = True
    return


def main():
    t = Thread(target=event_listener)
    t.start()
    update_steps()
    t.join()


if __name__ == '__main__':
    main()     
