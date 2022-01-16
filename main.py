# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os.path

import torch
import win32gui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import sys
import time
import os
hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t != "":
        print(h, t)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

app = QApplication(sys.argv)
screen = QApplication.primaryScreen()


def grabWindow(hwnd, output_file):
    img = screen.grabWindow(hwnd).toImage()
    img.save(output_file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    hwnd = 263182
    directory = "./grabImage"

    if not os.path.exists(directory):
        os.mkdir(directory)

    for i in range(10):
        t = time.time()
        hash_t = hash(t)
        path = f"%s/%d.jpeg" % (directory, hash_t)
        print(path)
        grabWindow(hwnd,  path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
