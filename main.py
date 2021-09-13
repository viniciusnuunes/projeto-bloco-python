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
import server as ServerInfo

ServerInfo.connectToServer()

pygame.font.init()
pygame.display.init()

screen = pygame.display.set_mode(
    (CONSTANT.SCREEN_WIDTH, CONSTANT.SCREEN_HEIGHT))
fontList = pygame.font.get_fonts()

PID = ServerInfo.sendMessage('pid')
HOSTS = ServerInfo.sendMessage('host')

if 'calibri' in fontList:
    font = 'calibri'
else:
    font = None

font = pygame.font.SysFont(font, 24)
pygame.display.set_caption('Gerenciador de tarefas')

clock = pygame.time.Clock()
count = 60

finished = False

screenList = [0, 1, 2, 3, 4, 5, 6, 7]
actualScreen = screenList[0]


while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        if count == 60:
            if actualScreen == 0:
                cpu = ServerInfo.sendMessage("cpu")
                CpuInfo.drawCpu(screen, font, cpu)
                count = 0

            if actualScreen == 1:
                disk = ServerInfo.sendMessage('disk')
                DiskInfo.drawDisk(screen, font, disk)
                count = 0

            if actualScreen == 2:
                memory = ServerInfo.sendMessage('memory')
                MemoryInfo.drawMemory(screen, font, memory)
                count = 0

            if actualScreen == 3:
                network = ServerInfo.sendMessage('network')
                NetworkInfo.drawNetwork(screen, font, network, HOSTS)
                count = 0

            if actualScreen == 4:
                resume = ServerInfo.sendMessage('resume')
                ResumeInfo.drawResume(screen, font, resume)
                count = 0

            if actualScreen == 5:
                files = ServerInfo.sendMessage('simple-files')
                SimpleFilesInfo.drawSimpleFiles(screen, font, files)
                count = 0

            if actualScreen == 6:
                files = ServerInfo.sendMessage('detailed-files')
                DetailedFilesInfo.drawDetailedFiles(screen, font, files)
                count = 0

            if actualScreen == 7:
                PidInfo.drawPid(screen, font, PID)
                count = 0

        if event.type == pygame.KEYDOWN:
            count = 59
            if event.key == pygame.K_LEFT:
                proxima_tela = screenList[actualScreen] - 1

                if proxima_tela < 0:
                    print('Não tem mais tela pra esquerda')
                    continue

                actualScreen = proxima_tela

            if event.key == pygame.K_RIGHT:
                proxima_tela = screenList[actualScreen] + 1

                if proxima_tela > 7:
                    print('Não tem mais tela pra direita')
                    continue

                actualScreen = proxima_tela

            if event.key == pygame.K_SPACE:
                proxima_tela = 4
                print('Vou para a tela TODOS')

                actualScreen = proxima_tela

            if event.key == pygame.K_F5 and actualScreen == 7:
                PID = ServerInfo.sendMessage('pid')
                print('PID Atualizado com sucesso...')
                PidInfo.drawPid(screen, font, PID)

        clock.tick(60)
        # pygame.display.update()
        pygame.display.flip()

        count += 1

ServerInfo.sendMessage('close-application')
pygame.display.quit()
