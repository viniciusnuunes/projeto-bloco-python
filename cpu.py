import pygame
import properties as CONSTANT

superior_surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA / 5))
inferior_surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, (CONSTANT.ALTURA_TELA / 5) * 4))


def exibeCpuCoreInfo(tela, font, data):
    __drawTopSurface(superior_surface, tela, font, data)
    __drawBottomSurface(inferior_surface, tela, data['cpu_percent'])


def __drawTopSurface(surface, tela, font, data):
    surface.fill(CONSTANT.PRETO)

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

    tela.blit(surface, (0, 0))


def __draw(surface, title, description, pos_y, font):
    text = title
    text = font.render(text, True, CONSTANT.BRANCO)
    surface.blit(text, (10, pos_y))

    text = description
    text = font.render(text, True, CONSTANT.BRANCO)
    surface.blit(text, (200, pos_y))


def __drawBottomSurface(surface, tela, cpuPercent):
    surface.fill(CONSTANT.PRETO)

    cpuLength = len(cpuPercent)
    x = y = 10
    desl = 10
    alt = surface.get_height() - 2*y
    larg = (surface.get_width()-2*y - (cpuLength+1)*desl)/cpuLength
    d = x + desl

    for i in cpuPercent:
        pygame.draw.rect(surface, CONSTANT.AZUL, (d, y, larg, alt))
        pygame.draw.rect(surface, CONSTANT.CINZA, 	(d, y, larg, (1-i/100)*alt))
        d = d + larg + desl

    tela.blit(surface, (0, CONSTANT.ALTURA_TELA/5))
