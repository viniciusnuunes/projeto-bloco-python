from inspect import getmembers
import socket
import sys
import pickle
import pygame
import properties as CONSTANT
import cpu_cores as CpuInfo
import disco as DiscoInfo
import memoria as MemoriaInfo
import rede as RedeInfo
import resumo as ResumoInfo
# import arquivos_simples as ArquivoSimplesInfo
# import arquivos_detalhado as ArquivoDetalhadoInfo
# import pid as PidInfo

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((CONSTANT.HOST, CONSTANT.PORT))

# Inicialização da tela e fonte
pygame.font.init()
pygame.display.init()

# Definições da tela, fonte e título da janela
tela = pygame.display.set_mode((CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))
lista_fontes = pygame.font.get_fonts()

if 'calibri' in lista_fontes:
    fonte = 'calibri'
else:
    fonte = None

font = pygame.font.SysFont(fonte, 24)
pygame.display.set_caption('Gerenciador de tarefas')

clock = pygame.time.Clock()
count = 60

finalizado = False


lista_telas = [0, 1, 2, 3, 4, 5, 6, 7]
tela_atual = lista_telas[0]


def getMessageFromServer(message):
    sock.send(message.encode('utf-8'))

    response = sock.recv(CONSTANT.BUFFER_SIZE)
    response = pickle.loads(response)

    return response


while not finalizado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizado = True

        if count == 60:
            if tela_atual == 0:
                cpu = getMessageFromServer("cpu")
                CpuInfo.exibeCpuCoreInfo(tela, font, cpu)
                count = 0
                
            if tela_atual == 1:
                disk = getMessageFromServer('disk')
                DiscoInfo.exibeDiscoInfo(tela, font, disk)
                count = 0
                
            if tela_atual == 2:
                memory = getMessageFromServer('memory')
                MemoriaInfo.exibeMemoriaInfo(tela, font, memory)
                count = 0
                
            if tela_atual == 3:
                network = getMessageFromServer('network')
                RedeInfo.exibeRedeInfo(tela, font, network)
                count = 0
                
            if tela_atual == 4:
                resume = getMessageFromServer('resume')
                ResumoInfo.exibeResumoInfo(tela, font, resume)
                count = 0
            
            # if tela_atual == 5:
            #     ArquivoSimplesInfo.exibeArquivosInfo(tela, font)
            #     count = 0
                
            # if tela_atual == 6:
            #     ArquivoDetalhadoInfo.exibeArquivosInfo(tela, font)
            #     count = 0
                
            # if tela_atual == 7:
            #     PidInfo.exibePidInfo(tela, font, PID)
            #     count = 0

        if event.type == pygame.KEYDOWN:
            count = 59
            if event.key == pygame.K_LEFT:
                proxima_tela = lista_telas[tela_atual] - 1

                if proxima_tela < 0:
                    print('Não tem mais tela pra esquerda')
                    continue

                tela_atual = proxima_tela

            if event.key == pygame.K_RIGHT:
                proxima_tela = lista_telas[tela_atual] + 1

                if proxima_tela > 7:
                    print('Não tem mais tela pra direita')
                    continue

                tela_atual = proxima_tela

            if event.key == pygame.K_SPACE:
                proxima_tela = 4
                print('Vou para a tela TODOS')

                tela_atual = proxima_tela

            # if event.key == pygame.K_F5 and tela_atual == 7:
            #     PID = CONSTANT.geraPid()
            #     print('PID Atualizado com sucesso...')
            #     PidInfo.exibePidInfo(tela, font, PID)

        clock.tick(60)
        # pygame.display.update()
        pygame.display.flip()

        count += 1

# getMessageFromServer('close-application')
getMessageFromServer('close-application')
sock.close()
pygame.display.quit()


# if tela_atual == 0:
#     info_cpu = getMessageFromServer("cpu")

# if tela_atual == 1:
#     info_disk = getMessageFromServer("disk")

# if tela_atual == 2:
#     info_memory = getMessageFromServer("memory")

# if tela_atual == 3:
#     info_network = getMessageFromServer("network")

# if tela_atual == 4:
#     info_resume = getMessageFromServer("resume")

# if tela_atual == 5:
#     info_simple_files = getMessageFromServer("simple-files")

# if tela_atual == 6:
#     info_detailed_files = getMessageFromServer("detailed-files")

# if tela_atual == 7:
#     info_pid = getMessageFromServer("pid")
