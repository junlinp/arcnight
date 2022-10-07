def RecvBytes(sock):
    data = bytes()
    len_bytes = sock.recv(4)
    length = int.from_bytes(len_bytes, byteorder="big")

    while len(data) < length:
        data = data + sock.recv(4096)
    return data

def SendBytes(sock, bytes):
    lens = len(bytes)
    lens_bytes = lens.to_bytes(4, byteorder = 'big')

    sock.send(lens_bytes)
    sock.send(bytes)