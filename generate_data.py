import cv2
import os
import numpy as np
import random
import threading

def load_image(path : str):
    img = cv2.imread(path)
    return img


def GaussianNoisy(image):
    row, col = image.shape
    mean = 0
    var = 0.1
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col))
    gauss = gauss.reshape(row, col)
    return image + gauss

def SaltNoisy(image, prob = 0.001):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):
                rdn = random.random()
                if rdn < prob:
                    output[i][j][k] = 0
                elif rdn > thres:
                    output[i][j][k] = 255
                else:
                    output[i][j][k] = image[i][j][k]
    return output

class OutputThread(threading.Thread):

    def __init__(self, output_dir, base_name, image, label_content, index):
        threading.Thread.__init__(self)

        self.output_dir_ = output_dir
        self.base_name_ = base_name
        self.image_ = image
        self.label_content_ = label_content
        self.index_ = index

    def run(self):
        cv2.imwrite(f"{self.output_dir_}/images/{self.base_name_}{self.index_}.png", SaltNoisy(self.image_))
        with open(f"{self.output_dir_}/labels/{self.base_name_}{self.index_}.txt","w") as f:
            f.write(self.label_content_)
        print(f"Generate {self.output_dir_}/images/{self.base_name_}{self.index_}.png")

def Generate(image_path : str, label_path : str, output_dir : str, base_name : str, num = 1024):

    if os.path.exists(output_dir) is False:
        os.mkdir(output_dir)
    
    if os.path.exists(f"{output_dir}/images") is False:
        os.mkdir(f"{output_dir}/images")

    if os.path.exists(f"{output_dir}/labels") is False:
        os.mkdir(f"{output_dir}/labels")

    img = load_image(image_path)
    
    with open(label_path, "r") as f:
        label_content = f.read()
    
    all_threads = [OutputThread(output_dir, base_name, img, label_content, i) for i in range(num)]

    for thread in all_threads:
        thread.start()

    for thread in all_threads:
        thread.join()




if __name__ == "__main__":


    Generate("/Users/panjunlin/repo/arcnight/dataset/begin.png", "/Users/panjunlin/repo/arcnight/dataset/begin.txt", "/Users/panjunlin/repo/arcnight/dataset/train", "begin", 128)
    Generate("/Users/panjunlin/repo/arcnight/dataset/end.png", "/Users/panjunlin/repo/arcnight/dataset/end.txt", "/Users/panjunlin/repo/arcnight/dataset/train", "end", 128)
    Generate("/Users/panjunlin/repo/arcnight/dataset/action.png", "/Users/panjunlin/repo/arcnight/dataset/action.txt", "/Users/panjunlin/repo/arcnight/dataset/train", "action", 128)
    Generate("/Users/panjunlin/repo/arcnight/dataset/begin_second.png", "/Users/panjunlin/repo/arcnight/dataset/begin.txt", "/Users/panjunlin/repo/arcnight/dataset/train", "begin_second", 128)
    Generate("/Users/panjunlin/repo/arcnight/dataset/end_second.png", "/Users/panjunlin/repo/arcnight/dataset/end.txt", "/Users/panjunlin/repo/arcnight/dataset/train", "end_second", 128)
    Generate("/Users/panjunlin/repo/arcnight/dataset/action_second.png", "/Users/panjunlin/repo/arcnight/dataset/action.txt", "/Users/panjunlin/repo/arcnight/dataset/train", "action_second", 128)


    Generate("/Users/panjunlin/repo/arcnight/dataset/begin.png", "/Users/panjunlin/repo/arcnight/dataset/begin.txt", "/Users/panjunlin/repo/arcnight/dataset/val", "begin", 64)
    Generate("/Users/panjunlin/repo/arcnight/dataset/end.png", "/Users/panjunlin/repo/arcnight/dataset/end.txt", "/Users/panjunlin/repo/arcnight/dataset/val", "end", 64)
    Generate("/Users/panjunlin/repo/arcnight/dataset/action.png", "/Users/panjunlin/repo/arcnight/dataset/action.txt", "/Users/panjunlin/repo/arcnight/dataset/val", "action", 64)

    Generate("/Users/panjunlin/repo/arcnight/dataset/begin.png", "/Users/panjunlin/repo/arcnight/dataset/begin.txt", "/Users/panjunlin/repo/arcnight/dataset/test", "begin", 32)
    Generate("/Users/panjunlin/repo/arcnight/dataset/end.png", "/Users/panjunlin/repo/arcnight/dataset/end.txt", "/Users/panjunlin/repo/arcnight/dataset/test", "end", 32)
    Generate("/Users/panjunlin/repo/arcnight/dataset/action.png", "/Users/panjunlin/repo/arcnight/dataset/action.txt", "/Users/panjunlin/repo/arcnight/dataset/test", "action", 32)
