import pyautogui
from tkinter import *
import time
import keyboard
import cv2
w = '0000,0000'
a = '0000,0000'
s = '0000,0000'
d = '0000,0000'
root = Tk()
root.title("app")
root.geometry("400x150+10+10")
root.configure(background='gold')
root.call('wm', 'attributes', '.', '-topmost', '1')
outputW = Label(root, text=f'{w= }',font='Helvetica 15 bold')
outputW.pack()
outputA = Label(root, text=f'{a= }',font='Helvetica 15 bold')
outputA.pack()
outputS = Label(root, text=f'{s= }',font='Helvetica 15 bold')
outputS.pack()
outputD = Label(root, text=f'{d= }',font='Helvetica 15 bold')
outputD.pack()



import win32api
count = 0
key_up, key_down = True, False
xclick, yclick = 0, 0
while True:
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    if state_left >=0:
        key_up = True
    else:
        key_up = False
        key_down = True

    if key_down and key_up:
        key_down = False
        xclick, yclick = win32api.GetCursorPos()
        print(xclick, yclick )
        count+=1
    if count == 1:
        w = str(xclick)+' , '+str(yclick)
        outputW.configure(text=f'{w= }')
    if count == 2:
        a = str(xclick) + ' , ' + str(yclick)
        outputA.configure(text=f'{a= }')
    if count == 3:
        s = str(xclick) + ' , ' + str(yclick)
        outputS.configure(text=f'{s= }')
    if count == 4:
        d = str(xclick) + ' , ' + str(yclick)
        outputD.configure(text=f'{d= }')
        root.update()
        with open('cordinates.txt','w') as sf:
            print(w+'\n'+a+'\n'+s+'\n'+d,file=sf)
        count+=1
        time.sleep(1)
        quit()

    root.update()