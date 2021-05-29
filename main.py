#import psutil
import pygame
import properties as CONSTAT
import cpu as CpuInfo

# Inicialização da tela e fonte
pygame.font.init()
pygame.display.init()

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


while not finalizado:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizado = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('Apertei a tecla pra esquerda')
            if event.key == pygame.K_SPACE:
                print('Apertei a barra de espaço')
            elif event.key == pygame.K_RIGHT:
                print('Apertei a tecla pra direita')

        if count == 60:
            CpuInfo.carrega_cpu_info(
                superior_surface, inferior_surface, tela, font)
            count = 0

        pygame.display.update()

        clock.tick(60)
        count += 1

pygame.display.quit()
