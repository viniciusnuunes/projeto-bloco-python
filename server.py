import socket
import pickle

HOST = 'localhost'
HOST_NAME = socket.gethostname()
PORT = 3000
BUFFER_SIZE = 4096

global sock


def connectToServer():
    global sock

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))


def sendMessage(message):
    global sock

    if message == 'close-application':
        sock.send(message.encode('utf-8'))
        sock.close()
        return

    sock.send(message.encode('utf-8'))

    response = sock.recv(BUFFER_SIZE)
    response = pickle.loads(response)

    return response
