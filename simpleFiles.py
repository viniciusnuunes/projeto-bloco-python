import pygame
import properties as CONSTANT

surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))


def exibeArquivosInfo(tela, font, data):
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))
    
    text = 'Arquivos e Pastas (Simples)'
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 10))

    textDistance = 40

    for file in data:
        text = font.render(file, 1, CONSTANT.BRANCO)
        tela.blit(text, (20, textDistance))
        textDistance += 20

