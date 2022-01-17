import os
import cv2
import numpy as np

def LoadImage(path):
    img = cv2.imread(path)
    return img

def LoadData(txt_path):
    with open(txt_path, "r") as f:
        lines = f.readlines()
        
        lines = map(lambda x : x[:-1].split(' '), lines)
        X = []
        y = []
        for item in lines:
            print(item)
            X.append(LoadImage(item[0]))
            y.append(item[1])

    return np.array(X), np.array(y)

if __name__ == "__main__":
    
    LoadData("./data/data.txt")

