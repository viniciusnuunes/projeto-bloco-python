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
tela_atual = lista_telas[0]

#try:
  #  if tela_atual == 0:
sock.connect((HOST, PORT))

sock.send('cpu-cores'.encode('utf-8'))

cpu_cores = sock.recv(BUFFER_SIZE)

cpu_cores = pickle.loads(cpu_cores)
print(cpu_cores)

sock.close()

# sock.connect((HOST, PORT))

# sock.send('cpu-percent'.encode('utf-8'))

# cpu_percent = sock.recv(BUFFER_SIZE)

# cpu_percent = pickle.loads(cpu_percent)
# print(cpu_percent)

# sock.close()
    # CpuCoreInfo.exibeCpuCoreInfo(tela, font)
    # count = 0

if tela_atual == 1:
    sock.connect((HOST, PORT))

    sock.send('disk'.encode('utf-8'))

    data = sock.recv(BUFFER_SIZE)

    data = pickle.loads(data)

    sock.close()
    # DiscoInfo.exibeDiscoInfo(tela, font)
    # count = 0

if tela_atual == 2:
    sock.connect((HOST, PORT))

    sock.send('memory'.encode('utf-8'))

    data = sock.recv(BUFFER_SIZE)

    data = pickle.loads(data)

    sock.close()
    # MemoriaInfo.exibeMemoriaInfo(tela, font)
    # count = 0

if tela_atual == 3:
    sock.connect((HOST, PORT))

    sock.send('network'.encode('utf-8'))

    data = sock.recv(BUFFER_SIZE)

    data = pickle.loads(data)

    sock.close()
    # RedeInfo.exibeRedeInfo(tela, font)
    # count = 0

if tela_atual == 4:
    sock.connect((HOST, PORT))

    sock.send('resume'.encode('utf-8'))

    data = sock.recv(BUFFER_SIZE)

    data = pickle.loads(data)

    sock.close()
    # ResumoInfo.exibeResumoInfo(tela, font)
    # count = 0

if tela_atual == 5:
    sock.connect((HOST, PORT))

    sock.send('simple-file'.encode('utf-8'))

    data = sock.recv(BUFFER_SIZE)

    data = pickle.loads(data)

    sock.close()
    # ArquivoSimplesInfo.exibeArquivosInfo(tela, font)
    # count = 0


if tela_atual == 6:
    sock.connect((HOST, PORT))

    sock.send('detailed-file'.encode('utf-8'))

    data = sock.recv(BUFFER_SIZE)

    data = pickle.loads(data)

    sock.close()
    # ArquivoDetalhadoInfo.exibeArquivosInfo(tela, font)
    # count = 0

if tela_atual == 7:
    sock.connect((HOST, PORT))

    sock.send('pid'.encode('utf-8'))

    data = sock.recv(BUFFER_SIZE)

    data = pickle.loads(data)

    sock.close()
    # PidInfo.exibePidInfo(tela, font, PID)
    # count = 0
    
# except Exception as error:
#     print(str(error))
#     sys.exit(1)

