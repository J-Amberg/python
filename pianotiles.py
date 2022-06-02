#Bot made to play this game here: https://lagged.com/play/1461/
#My highscore is 334
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import pyautogui

#Tile 1 Position: X:  729 Y:  266 RGB: (211, 211, 211)
#Tile 2 Position: X:  824 Y:  222 RGB: ( 74,  74,  86)
#Tile 3 Position: X: 1073 Y:  247 RGB: (211, 211, 211)
#Tile 4 Position: X: 1231 Y:  228 RGB: ( 74,  74,  86)
#Tile 5 Position: X:  702 Y:  416 RGB: (211, 211, 211)
#Tile 6 Position: X:  892 Y:  405 RGB: (211, 211, 211)
#Tile 7 Position: X: 1076 Y:  412 RGB: (211, 211, 211)
#Tile 8 Position: X: 1218 Y:  409 RGB: (211, 211, 211)
#Tile 9 Position: X:  740 Y:  565 RGB: (211, 211, 211)
#Tile 10 Position: X:  926 Y:  586 RGB: (211, 211, 211)
#Tile 11 Position: X: 1071 Y:  596 RGB: (211, 211, 211)
#Tile 12 Position: X: 1192 Y:  584 RGB: (211, 211, 211)
#Tile 13 Position: X:  731 Y:  753 RGB: (211, 211, 211)
#Tile 14 Position: X:  915 Y:  749 RGB: (211, 211, 211)
#Tile 15 Position: X:  998 Y:  751 RGB: (211, 211, 211)
#Tile 16 Position: X: 1202 Y:  735 RGB: ( 74,  74,  86)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    #Tiles 1-4
    if pyautogui.pixel(729, 266)[0] == (74):
        click(729,266)
    if pyautogui.pixel(824, 222)[0] == (74):
        click(824,222)
    if pyautogui.pixel(1073, 247)[0] == (74):
        click(1073,247)
    if pyautogui.pixel(1231,228)[0] == (74):
        click(1231,228)
    #Tiles 5-8
    if pyautogui.pixel(702, 416)[0] == (74):
        click(702,416)
    if pyautogui.pixel(892, 405)[0] == (74):
        click(892,405)
    if pyautogui.pixel(1076, 412)[0] == (74):
        click(1076,412)
    if pyautogui.pixel(1218, 409)[0] == (74):
        click(1218,409)
    #Tiles 9-12
    if pyautogui.pixel(740, 565)[0] == (74):
        click(740,565)
    if pyautogui.pixel(926, 565)[0] == (74):
        click(926,565)
    if pyautogui.pixel(1071, 565)[0] == (74):
        click(1071,565)
    if pyautogui.pixel(1192, 565)[0] == (74):
        click(1192,565)
    #Tiles 13-16
    if pyautogui.pixel(731, 753)[0] == (74):
        click(731,753)
    if pyautogui.pixel(926, 753)[0] == (74):
        click(926,753)
    if pyautogui.pixel(1071, 753)[0] == (74):
        click(1071,753)
    if pyautogui.pixel(1192, 753)[0] == (74):
        click(1192,753)
