import pygame
import properties as CONSTANT

surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))


def exibeMemoriaInfo(tela, font, data):
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))

    totalMemory = data['memory_total']
    useMemory = data['memory_use']
    freeMemory = data['memory_free']
    percentMemory = data['memory_percent']

    totalMemory = round(totalMemory / (1024*1024*1024), 2)
    useMemory = round(useMemory / (1024*1024*1024), 2)
    freeMemory = round(freeMemory / (1024*1024*1024), 2)

    width = (totalMemory) - \
        (useMemory)

    # desenhando a barra de memória
    totalWidth = CONSTANT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTANT.CINZA, (20, 50, totalWidth, 30))
    tela.blit(surface, (0, 90))

    # desenhando a barra de uso de memória
    width = totalWidth * percentMemory / 100
    pygame.draw.rect(surface, CONSTANT.AZUL, (20, 50, width, 30))
    tela.blit(surface, (0, 90))

    text = "Total de Memória: " + str(totalMemory) + " GB"
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 10))

    text = "Usado: " + str(useMemory)+" GB"
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 40))

    text = "Livre: " + str(freeMemory)+" GB"
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 70))

    text = "Uso de Memória: " + str(percentMemory) + "%"
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 100))
