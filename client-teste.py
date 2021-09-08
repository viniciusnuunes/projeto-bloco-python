import socket
import sys
import pickle
import pygame
import properties as CONSTANT

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((CONSTANT.HOST, CONSTANT.PORT))

# multiProcessingQueue = multiprocessing.Queue()

    # response = sock.recv(CONSTANT.BUFFER_SIZE)
    # response = pickle.loads(response)   
    
    # return response


for i in range(10):    
    sock.send('cpu'.encode('utf-8'))
    res = sock.recv(CONSTANT.BUFFER_SIZE)
    # res = pickle.loads(res)
    res = res.decode('utf-8')
    
    print('>>>>>>>>>>>>>>>>>>>>>>>> ', i, res)
    print('---------------------------------')

# sock.send('cpu'.encode('utf-8'))

sock.send('close-application'.encode('utf-8'))
sock.close()
