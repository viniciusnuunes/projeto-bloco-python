import pygame
import properties as CONSTANT

topSurface = pygame.surface.Surface(
    (CONSTANT.SCREEN_WIDTH, CONSTANT.SCREEN_HEIGHT / 5))
bottomSurface = pygame.surface.Surface(
    (CONSTANT.SCREEN_WIDTH, (CONSTANT.SCREEN_HEIGHT / 5) * 4))


def drawCpu(screen, font, data):
    __drawTopSurface(topSurface, screen, font, data)
    __drawBottomSurface(bottomSurface, screen, data['cpu_percent'])


def __drawTopSurface(surface, screen, font, data):
    surface.fill(CONSTANT.BLACK)

    brand = data['cpu_brand']
    __draw(surface, 'Nome:', brand, 10, font)

    arch = str(data['cpu_architecture'])
    __draw(surface, 'Arquitetura:', arch, 30, font)

    bits = str(data['cpu_bits'])
    __draw(surface, 'Palavra (bits):', bits, 50, font)

    freq = str(data['cpu_frequency'])
    __draw(surface, 'Frequência:', freq, 70, font)

    totalCores = str(data['cpu_count_all_cores'])
    physicalCores = str(data['cpu_count_physical_cores'])
    __draw(surface, 'Núcleos (físicos):',
           f'{totalCores}({physicalCores})', 90, font)

    screen.blit(surface, (0, 0))


def __draw(surface, title, description, pos_y, font):
    text = title
    text = font.render(text, True, CONSTANT.WHITE)
    surface.blit(text, (10, pos_y))

    text = description
    text = font.render(text, True, CONSTANT.WHITE)
    surface.blit(text, (200, pos_y))


def __drawBottomSurface(surface, tela, cpuPercent):
    surface.fill(CONSTANT.BLACK)

    cpuLength = len(cpuPercent)
    x = y = 10
    desl = 10
    alt = surface.get_height() - 2*y
    larg = (surface.get_width()-2*y - (cpuLength+1)*desl)/cpuLength
    d = x + desl

    for i in cpuPercent:
        pygame.draw.rect(surface, CONSTANT.BLUE, (d, y, larg, alt))
        pygame.draw.rect(surface, CONSTANT.GRAY, 	(d, y, larg, (1-i/100)*alt))
        d = d + larg + desl

    tela.blit(surface, (0, CONSTANT.SCREEN_HEIGHT/5))
