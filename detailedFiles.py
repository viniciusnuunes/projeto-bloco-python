import pygame
import time
import properties as CONSTANT

surface = pygame.surface.Surface(
    (CONSTANT.SCREEN_WIDTH, CONSTANT.SCREEN_HEIGHT))


def drawDetailedFiles(screen, font, data):
    surface.fill(CONSTANT.BLACK)
    screen.blit(surface, (0, 0))

    text = 'Arquivos e Pastas (Detalhado)'
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 10))

    text = '{:30}'.format("Nome")
    text = text + '{:11}'.format("Tamanho")
    text = text + '{:27}'.format("Data de Modificação")
    text = text + '{:27}'.format("Data de Criação")

    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 40))

    textDistance = 70

    for file in data:
        kb = (data[file][0])/1000
        size = '{:10}'.format(str('{:.2f}'.format(kb)) + ' KB')
        fileName = '{:27}'.format(file)

        text = fileName + " " + size + \
            time.ctime(data[file][2]) + \
            time.ctime(data[file][1])

        text = font.render(text, 1, CONSTANT.WHITE)
        screen.blit(text, (20, textDistance))
        textDistance += 20
