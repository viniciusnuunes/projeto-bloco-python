import socket
import pygame
import properties as CONSTANT
import cpu as CpuInfo
import disk as DiskInfo
import memory as MemoryInfo
import network as NetworkInfo
import resume as ResumeInfo
import simpleFiles as SimpleFilesInfo
import detailedFiles as DetailedFilesInfo
import pid as PidInfo
import getServerInformation as Server

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((CONSTANT.HOST, CONSTANT.PORT))

pygame.font.init()
pygame.display.init()

tela = pygame.display.set_mode((CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))
lista_fontes = pygame.font.get_fonts()

PID = Server.connectToServer(sock, 'pid')

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


while not finalizado:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizado = True

        if count == 60:
            if tela_atual == 0:
                cpu = Server.connectToServer(sock, "cpu")
                CpuInfo.exibeCpuCoreInfo(tela, font, cpu)
                count = 0
                
            if tela_atual == 1:
                disk = Server.connectToServer(sock, 'disk')
                DiskInfo.exibeDiscoInfo(tela, font, disk)
                count = 0
                
            if tela_atual == 2:
                memory = Server.connectToServer(sock, 'memory')
                MemoryInfo.exibeMemoriaInfo(tela, font, memory)
                count = 0
                
            if tela_atual == 3:
                network = Server.connectToServer(sock, 'network')
                NetworkInfo.exibeRedeInfo(tela, font, network)
                count = 0
                
            if tela_atual == 4:
                resume = Server.connectToServer(sock, 'resume')
                ResumeInfo.exibeResumoInfo(tela, font, resume)
                count = 0
            
            if tela_atual == 5:
                files = Server.connectToServer(sock, 'simple-files')
                SimpleFilesInfo.exibeArquivosInfo(tela, font, files)
                count = 0
                
            if tela_atual == 6:
                files = Server.connectToServer(sock, 'detailed-files')
                DetailedFilesInfo.exibeArquivosInfo(tela, font, files)
                count = 0
                
            if tela_atual == 7:
                PidInfo.exibePidInfo(tela, font, PID)
                count = 0

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

            if event.key == pygame.K_F5 and tela_atual == 7:
                PID = Server.connectToServer(sock, 'pid')
                print('PID Atualizado com sucesso...')
                PidInfo.exibePidInfo(tela, font, PID)

        clock.tick(60)
        # pygame.display.update()
        pygame.display.flip()

        count += 1

Server.connectToServer(sock, 'close-application')
sock.close()
pygame.display.quit()