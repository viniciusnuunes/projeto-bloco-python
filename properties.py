import psutil
import random


def geraPid():
    __lista_de_pids = psutil.pids()
    __pid_aleatorio = random.randint(0, len(__lista_de_pids))
    __pid_escolhido = __lista_de_pids[__pid_aleatorio]

    print('PID escoliho: ', __pid_escolhido)

    return psutil.Process(__pid_escolhido)


PID = geraPid()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (100, 100, 100)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

LARGURA_TELA = 800
ALTURA_TELA = 600
