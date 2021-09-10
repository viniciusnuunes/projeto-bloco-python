import pygame
import properties as CONSTANT

surface = pygame.surface.Surface(
    (CONSTANT.SCREEN_WIDTH, CONSTANT.SCREEN_HEIGHT))


def drawSimpleFiles(screen, font, data):
    surface.fill(CONSTANT.BLACK)
    screen.blit(surface, (0, 0))
    
    text = 'Arquivos e Pastas (Simples)'
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 10))

    textDistance = 40

    for file in data:
        text = font.render(file, 1, CONSTANT.WHITE)
        screen.blit(text, (20, textDistance))
        textDistance += 20

