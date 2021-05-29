#import psutil
import pygame
import properties as CONSTAT
import cpu_cores as CpuCoreInfo

# Inicialização da tela e fonte
pygame.font.init()
pygame.display.init()

lista_telas = [0, 1, 2, 3, 4]

# Definições da tela, fonte e título da janela
tela = pygame.display.set_mode((CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA))
font = pygame.font.Font(None, 28)
pygame.display.set_caption('Gerenciador de tarefas')

# Tela superior e inferior
superior_surface = pygame.surface.Surface(
    (CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA / 5))
inferior_surface = pygame.surface.Surface(
    (CONSTAT.LARGURA_TELA, (CONSTAT.ALTURA_TELA / 5) * 4))

clock = pygame.time.Clock()
count = 60

finalizado = False

tela_atual = lista_telas[0]

while not finalizado:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizado = True

        if tela_atual == 0:
            print('Tela de CPU')
            if count == 60:
                CpuCoreInfo.exibeCpuCoreInfo(
                    superior_surface, inferior_surface, tela, font)
                count = 0

        if tela_atual == 1:
            print('Tela de disco')
        if tela_atual == 2:
            print('Tela de MEMORIA')
        if tela_atual == 3:
            print('Tela de REDE')
        if tela_atual == 4:
            print('Tela de TODAS')

        if event.type == pygame.KEYDOWN:
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

        clock.tick(60)
        count += 1

pygame.display.quit()
