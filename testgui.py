import tkinter as tk
import win32api, win32con
import time
from pynput import mouse


cordinates = []
cordinatesPet = []
with open('cordinates.txt','r') as ff:
    for sor in ff:
        cordinates.append(sor.strip().split())

with open('petcordinates.txt') as ff:
    cordinatesPet = ff.read().split(',')
print(cordinatesPet)
print(cordinates)

root = tk.Tk()
root.attributes('-fullscreen',True)
root.configure(background="black")
wplace1 = tk.Label(text='W')
wplace1.place(x=cordinates[0][0], y=cordinates[0][2])
aplace1 = tk.Label(text='A')
aplace1.place(x=cordinates[1][0], y=cordinates[1][2])
splace1 = tk.Label(text='S')
splace1.place(x=cordinates[2][0], y=cordinates[2][2])
dplace1 = tk.Label(text='D')
dplace1.place(x=cordinates[3][0], y=cordinates[3][2])
root.attributes('-alpha',0.2)





root.mainloop()