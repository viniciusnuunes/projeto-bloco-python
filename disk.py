import pygame
import properties as CONSTANT

surface = pygame.surface.Surface(
    (CONSTANT.SCREEN_WIDTH, CONSTANT.SCREEN_HEIGHT))



def drawDisk(screen, font, data):
    surface.fill(CONSTANT.BLACK)
    screen.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de disco
    largura = CONSTANT.SCREEN_WIDTH - 2 * 20
    pygame.draw.rect(surface, CONSTANT.GRAY, (20, 50, largura, 30))
    screen.blit(surface, (0, 90))
    
    largura = largura * data['disk_percent'] / 100
    pygame.draw.rect(surface, CONSTANT.BLUE, (20, 50, largura, 30))
    screen.blit(surface, (0, 90))

    # Capacidade total do disco
    texto_total = "Total do Disco: (" + \
        str(round(data['disk_total']/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 10))

    # Desenhando o texto acima da barra de uso de disco
    texto_barra = "Usado: (" + str(data['disk_percent'])+" %):"
    text = font.render(texto_barra, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 40))

    # Espaço livre do disco
    texto_livre = "Livre: (" + str(round(data['disk_free'] /
                                         (1024*1024*1024), 2))+" GB):"
    text = font.render(texto_livre, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 70))

    # Porcentagem de uso do disco
    texto_barra = "Porcentagem de uso de Disco: (" + \
        str(data['disk_percent'])+" %):"
    text = font.render(texto_barra, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 100))
