import os
import cv2

def LoadImage(path):
    img = cv2.imread(path)
    return img

def ListDir(dir_path):
