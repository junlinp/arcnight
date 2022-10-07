import os.path
import torch
import sys
import time
import os
import cv2





def load_model(model_path : str):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
    return model

def load_image(image_path : str) :
    img = cv2.imread(image_path)
    return img



if __name__ == '__main__':

    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} path/to/model.pt path/to/image path/to/output")
    else:
        img = load_image(sys.argv[2])
        model = load_model(sys.argv[1])

        result = model(img)

        print(result.xyxy[0])

        first_result = result.xyxy[0]

        if len(first_result) > 0:
            print(result.xyxy[0][0][0])
            print(result.xyxy[0][0][1])
            x = 0.5 * (result.xyxy[0][0][0] + result.xyxy[0][0][2])
            y = 0.5 * (result.xyxy[0][0][1] + result.xyxy[0][0][3])
            with open(sys.argv[3], "w") as f:
                f.write(f"{x.item()} {y.item()}")
            #result.show()
        else:
            print("-1 -1")
