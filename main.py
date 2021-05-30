#import psutil
import pygame
import properties as CONSTAT
import cpu_cores as CpuCoreInfo
import disco as DiscoInfo
import memoria as MemoriaInfo

# Inicialização da tela e fonte
pygame.font.init()
pygame.display.init()

lista_telas = [0, 1, 2, 3, 4]

# Definições da tela, fonte e título da janela
tela = pygame.display.set_mode((CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA))
font = pygame.font.Font(None, 28)
pygame.display.set_caption('Gerenciador de tarefas')

clock = pygame.time.Clock()
count = 30

finalizado = False

tela_atual = lista_telas[0]

while not finalizado:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizado = True

        if count == 30:
            if tela_atual == 0:
                CpuCoreInfo.exibeCpuCoreInfo(tela, font)
                count = 0

            if tela_atual == 1:
                DiscoInfo.exibeDiscoInfo(tela, font)
                count = 0

            if tela_atual == 2:
                MemoriaInfo.exibeMemoriaInfo(tela, font)
                cout = 0

            count = 0

        if tela_atual == 3:
            print('Tela de REDE')
        if tela_atual == 4:
            print('Tela de TODAS')

        if event.type == pygame.KEYDOWN:
            count = 29
            if event.key == pygame.K_LEFT:
                proxima_tela = lista_telas[tela_atual] - 1

                if proxima_tela < 0:
                    print('Não tem mais tela pra esquerda')
                    continue

                tela_atual = proxima_tela

            if event.key == pygame.K_RIGHT:
                proxima_tela = lista_telas[tela_atual] + 1

                if proxima_tela > 4:
                    print('Não tem mais tela pra direita')
                    continue

                tela_atual = proxima_tela

            elif event.key == pygame.K_SPACE:
                proxima_tela = 4
                print('Vou para a ultima tela (tela Todos)')

                tela_atual = proxima_tela

        pygame.display.update()

        clock.tick(30)
        count += 1

pygame.display.quit()
