import pyautogui
from tkinter import *
import time
import keyboard
import cv2
import win32api
w = '0000,0000'
a = '0000,0000'
s = '0000,0000'
d = '0000,0000'
root = Tk()
root.title("app")
root.geometry("400x150+10+10")
root.configure(background='gold')
root.call('wm', 'attributes', '.', '-topmost', '1')

start = True
bekert = ''
print('Select the start option:\n 1. Get the golden ticket and pet and choose cordinate\n 2. Get the dance game arrows cordinates\n 3. Get the claim cordinate')
while start:
    bekert = input('1 / 2 / 3 : ')
    if bekert in ('1', '2', '3'):
        bekert = int(bekert)
        start = False


if bekert == 1:
    key_up, key_down = True, False
    xclick, yclick = 0, 0
    pet, ticket, choose = [], [], []
    futas = 0
    outputticket = Label(root, text=f'{ticket= }', font='Helvetica 15 bold')
    outputticket.pack()
    outputPet = Label(root, text=f'{pet= }', font='Helvetica 15 bold')
    outputPet.pack()
    outputchoose = Label(root, text=f'{choose= }', font='Helvetica 15 bold')
    outputchoose.pack()

    while True:
        state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
        if state_left >= 0:
            key_up = True
        else:
            key_up = False
            key_down = True

        if key_down and key_up:
            key_down = False
            xclick, yclick = win32api.GetCursorPos()
            futas += 1
        if keyboard.is_pressed('s'):
            with open('petcordinates.txt','w') as sf:
                sf.write(','.join(ticket)+':')
                sf.write(','.join(pet)+':')
                sf.write(','.join(choose))
            outputSAVE = Label(root, text='CORDINATES SAVED', font='Helvetica 15 bold')
            outputSAVE.pack()
            root.update()
            time.sleep(0.4)
            outputSAVE.pack_forget()
        if futas == 1:
            ticket = [str(xclick), str(yclick)]
            outputticket.configure(text=f'{ticket= }')
        elif futas ==2:
            pet = [str(xclick), str(yclick)]
            outputPet.configure(text=f'{pet= }')
        elif futas == 3:
            choose = [str(xclick), str(yclick)]
            outputchoose.configure(text=f'{choose= }')
            futas = 0
        root.update()


elif bekert == 2:
    count = 0
    key_up, key_down = True, False
    xclick, yclick = 0, 0
    outputW = Label(root, text=f'{w= }', font='Helvetica 15 bold')
    outputW.pack()
    outputA = Label(root, text=f'{a= }', font='Helvetica 15 bold')
    outputA.pack()
    outputS = Label(root, text=f'{s= }', font='Helvetica 15 bold')
    outputS.pack()
    outputD = Label(root, text=f'{d= }', font='Helvetica 15 bold')
    outputD.pack()
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
elif bekert == 3:
    key_up, key_down = True, False
    xclick, yclick = 0, 0
    claim = []
    outputclaim = Label(root, text=f'{claim= }', font='Helvetica 15 bold')
    outputclaim.pack()
    while True:
        state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
        if state_left >= 0:
            key_up = True
        else:
            key_up = False
            key_down = True

        if key_down and key_up:
            key_down = False
            xclick, yclick = win32api.GetCursorPos()
            claim = [str(xclick), str(yclick)]
            outputclaim.configure(text=f'{claim= }')
            root.update()
        if keyboard.is_pressed('s'):
            with open('claimcordinates.txt','w') as sf:
                sf.write(','.join(claim))
            outputSAVE = Label(root, text='CORDINATES SAVED', font='Helvetica 15 bold')
            outputSAVE.pack()
            root.update()
            time.sleep(0.4)
            outputSAVE.pack_forget()
        root.update()