#!/usr/bin/python3
# -*- coding:UTF-8 -*-
from tkinter import *
from os import *
root=Tk()
root.title("GPIO test")

def btn_on_click():
    system("sudo ./power.sh 2 1")
def btn_off_click():
    system("sudo ./power.sh 2 0")
btn_on=Button(root,text="power on",command=btn_on_click)
btn_on.pack();

btn_off=Button(root,text="power off",command=btn_off_click)
btn_off.pack();

root.mainloop()
