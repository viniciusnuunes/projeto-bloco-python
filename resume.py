import pygame
import properties as CONSTANT

surface = pygame.surface.Surface(
    (CONSTANT.SCREEN_WIDTH, CONSTANT.SCREEN_HEIGHT))


def drawResume(screen, font, data):
    surface.fill(CONSTANT.BLACK)
    screen.blit(surface, (0, 0))

    # Barra total de disco
    width = CONSTANT.SCREEN_WIDTH - 2 * 20
    pygame.draw.rect(surface, CONSTANT.GRAY, (20, 50, width, 30))
    screen.blit(surface, (0, 60))

    # Barra de uso de disco
    width = width * data['disk_percent'] / 100
    pygame.draw.rect(surface, CONSTANT.BLUE, (20, 50, width, 30))
    screen.blit(surface, (0, 60))

    # Barra total de memoria
    width = CONSTANT.SCREEN_WIDTH - 2 * 20
    pygame.draw.rect(surface, CONSTANT.GRAY, (20, 50, width, 30))
    screen.blit(surface, (0, 150))

    # Barra uso de memoria
    width = width * data['memory_percent'] / 100
    pygame.draw.rect(surface, CONSTANT.BLUE, (20, 50, width, 30))
    screen.blit(surface, (0, 150))

    # Texto
    text = 'CPU: ' + data['cpu_name']
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 10))

    # Texto
    text = 'IP: ' + data['ip']
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 40))

    # Texto
    totalDisk = data['disk_total']
    totalDisk = str(round(totalDisk/(1024*1024*1024), 2))

    texto_total = 'Total do Disco: ' + totalDisk + 'GB'
    text = font.render(texto_total, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 70))

    # Texto
    memoryUse = data['memory_use']
    memoryTotal = data['memory_total']

    memoryUse = str(round(memoryUse/(1024*1024*1024), 2))
    memoryTotal = str(round(memoryTotal/(1024*1024*1024), 2))

    texto_total = 'Memória total: ' + memoryTotal + 'GB - Em Uso: ' + memoryUse + 'GB'
    text = font.render(texto_total, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 160))
