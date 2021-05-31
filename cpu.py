import psutil
import pygame
import platform
import properties as CONSTAT

cpu_surface = pygame.surface.Surface(
    (CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA))

todas_surface = pygame.surface.Surface((CONSTAT.LARGURA_TELA, (CONSTAT.ALTURA_TELA / 4)))

cpu_info = psutil.cpu_percent(interval=0)

def exibeCpuTodas(tela, font, surface_pos_x, surface_pos_y):
    __desenha_barra_cpu(todas_surface, tela, font, surface_pos_x, surface_pos_y)

def exibeCpuSimplificada(tela, font):
    __desenha_barra_cpu(cpu_surface, tela, font)


def __desenha_barra_cpu(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTAT.PRETO)
    tela.blit(surface, (0, 0))

    # Desenhando a barra de CPU
    largura = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 70))
    tela.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de CPU
    largura = largura * cpu_info/100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 70))
    tela.blit(surface, (0, 0))

    # Desenhando o texto acima da barra de CPU
    texto_barra = "Uso de CPU: (" + str(cpu_info) + " %):"
    texto_proc = "Cpu: (" + str(platform.processor()) + "):"
    text = font.render(texto_barra, 1, CONSTAT.BRANCO)
    text_proc = font.render(texto_proc, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 0))
    tela.blit(text_proc, (20, 25))
