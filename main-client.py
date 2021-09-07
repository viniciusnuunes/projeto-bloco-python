import socket
import sys
import pickle
import pygame
# import properties as CONSTANT
# import cpu_cores as CpuCoreInfo
# import disco as DiscoInfo
# import memoria as MemoriaInfo
# import rede as RedeInfo
# import resumo as ResumoInfo
# import arquivos_simples as ArquivoSimplesInfo
# import arquivos_detalhado as ArquivoDetalhadoInfo
# import pid as PidInfo

HOST = 'localhost'
HOST_NAME = socket.gethostname()
PORT = 3000
BUFFER_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

lista_telas = [0, 1, 2, 3, 4, 5, 6, 7]
tela_atual = lista_telas[7]

# conecta, manda mensagem, recebe resposta, descompacta resposta, fecha conexão, retorna a resposta


def info(message):
    sock.connect((HOST, PORT))

    sock.send(message.encode('utf-8'))

    response = sock.recv(BUFFER_SIZE)

    response = pickle.loads(response)
    print(response)

    sock.close()

    # exibir informações solicitada

    return response

if tela_atual == 0:
    info_cpu = info("cpu")

if tela_atual == 1:
    info_disk = info("disk")

if tela_atual == 2:
    info_memory = info("memory")

if tela_atual == 3:
    info_network = info("network")

if tela_atual == 4:
    info_resume = info("resume")

if tela_atual == 5:
    info_simple_files = info("simple-files")

if tela_atual == 6:
    info_detailed_files = info("detailed-files")

if tela_atual == 7:
    info_pid = info("pid")
