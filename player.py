import pyautogui
import time
import keyboard
import cv2
from tkinter import *

debugg = True


def reset():
    global darab, nyomni
    darab = 2
    nyomni = []
    print(darab, nyomni)


def debug():
    global darab, nyomni
    darab += 1
    nyomni.append('W')
    print(darab, nyomni)


colors = [[0, 166, 236], [255, 215, 29], [255, 70, 70], [67,234,55]]
keys = ['W','A','S','D']
blue = [0, 166, 236]
green = [67,234,55]
red = [255, 70, 70]
yellow = [255, 215, 29]

cordinates = []
with open('cordinates.txt','r') as ff:
    for sor in ff:
        cordinates.append(sor.strip().split())

print(cordinates)
for adat in range(len(cordinates)):
    cordinates[adat].pop(1)
    cordinates[adat].append(colors[adat])
    cordinates[adat].append(keys[adat])
    print(cordinates)
root = Tk()
root.title("app")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("600x150+10+10")
root.configure(background='gold')
root.call('wm', 'attributes', '.', '-topmost', '1')
output = Label(root, text='HELLO', font='Helvetica 15 bold')
output.pack()
button = Button(root, text='RESET', command=reset)
button.pack()
if debugg:
    button2 = Button(root, text='DEBUG', command=debug)
    button2.pack()
root.update()

betuk = []
nyomni = []
elozolat = 0
darab = 2
while True:
    lat = 0
    if darab == len(nyomni):
        time.sleep(1.2)
        for betu in nyomni:
            if betu == "W":
                keyboard.press('w')
                time.sleep(0.01)
                keyboard.release('w')
            if betu == "A":
                keyboard.press('a')
                time.sleep(0.01)
                keyboard.release('a')
            if betu == "S":
                keyboard.press('s')
                time.sleep(0.01)
                keyboard.release('s')
            if betu == "D":
                keyboard.press('d')
                time.sleep(0.01)
                keyboard.release('d')
        output.configure(text=f'')
        root.update()
        nyomni = []
        darab += 1
        print(darab)
    elif darab == 7:
        reset()
        keyboard.press('f')
        time.sleep(0.01)
        keyboard.release('f')

    else:
        for d in cordinates:
            x, y = d[0],d[1]
            r, g, b = d[2]
            #print(x,y)
            #print(r,g,b)
            color = pyautogui.pixel(int(x),int(y))
            most = 1
            if color[0] == r and color[1] == g and color[2] == b:
                betuk.append(d[3])
                lat += 1
        if lat != 1 and elozolat ==1:
            nyomni.append(betuk[-1])
        elozolat = lat
        output.configure(text=f'{nyomni}')
        root.update()
