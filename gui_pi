#!/usr/bin/python3
# -*- coding:UTF-8 -*-
from tkinter import *
from os import *
root=Tk()
root.title("GPIO test")

def btn_on_click():
    system("sudo raspi-gpio set 2 op")
    system("sudo raspi-gpio set 2 dh")
def btn_off_click():
    system("sudo raspi-gpio set 2 op")
    system("sudo raspi-gpio set 2 dl")
btn_on=Button(root,width=30,height=5,text="power on",command=btn_on_click)
btn_on.pack();
btn_off=Button(root,width=30,height=5,text="power off",command=btn_off_click)
btn_off.pack();

root.mainloop()
