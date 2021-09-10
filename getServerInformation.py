import pickle
import properties as CONSTANT

def connectToServer(sock, message):
    sock.send(message.encode('utf-8'))

    response = sock.recv(CONSTANT.BUFFER_SIZE)
    response = pickle.loads(response)

    return response