import sys
import pickle
import cv2
import socket
from socket_utils import SendBytes, RecvBytes

import torch

def load_image(image_path : str) :
    img = cv2.imread(image_path)
    return img

def SendImage(socket_, img):

    bytes = pickle.dumps(img)

    SendBytes(socket_, bytes)

def RecvTensor(socket_):
    bytes = RecvBytes(socket_)
    return pickle.loads(bytes)

if __name__ == "__main__":

    if len(sys.argv) < 5:
        print(f"Usage: {sys.argv[0]} server_url port path/to/image path/to/output")
    else:
        image_path = sys.argv[3]
        img = load_image(image_path)
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((sys.argv[1], int(sys.argv[2])))

        SendImage(clientSocket, img)

        result_tensor = RecvTensor(clientSocket)
        output_path = sys.argv[4]
        if result_tensor[4] > 0:
            x_min = result_tensor[0]
            y_min = result_tensor[1]
            x_max = result_tensor[2]
            y_max = result_tensor[3]
            class_type = result_tensor[4]

            x = (x_min + x_max) * 0.5
            y = (y_min + y_max) * 0.5
            print(f"Result : {result_tensor}")
            with open(output_path, "w") as f:
                f.write(f"{x} {y}")
        else:
            print("No result") 






