import sys
import socket
import os
import pickle
import torch
from socket_utils import SendBytes, RecvBytes

def ParseFromSocket(sock):
    data = RecvBytes(sock)
    return pickle.loads(data)

def load_model(model_path : str):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
    return model

def SendInferenceResult(sock, result):
    result_tensor = result
    tensor = result_tensor.xyxy[0]
    res = ()
    if len(tensor) > 0:
        res = [t.item() for t in tensor[0]]
    else:
        res = [-1, -1, -1, -1, -1]
    bytes = pickle.dumps(res)
    SendBytes(sock, bytes)

    
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} path/to/model")
    else:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Port = 12345
        model = load_model(sys.argv[1])
        print(f"Start Server On 0.0.0.0:{Port}")
        serverSocket.bind(("0.0.0.0", Port))
        serverSocket.listen()

        while True:
            (clientConnected, clientAddress) = serverSocket.accept()
            print("Accepted a connection request from {}".format(clientAddress))

            recv_img = ParseFromSocket(clientConnected)

            result = model(recv_img)

            SendInferenceResult(clientConnected, result)
        