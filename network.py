import pygame
import properties as CONSTANT

surface = pygame.surface.Surface(
    (CONSTANT.SCREEN_WIDTH, CONSTANT.SCREEN_HEIGHT))


def drawNetwork(screen, font, data):
    surface.fill(CONSTANT.BLACK)
    screen.blit(surface, (0, 0))

    text = 'IP: ' + data['ip_pc']
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 10))

    text = 'Mascara: ' + data['ip_mask']
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 40))

    text = 'Endereço Físico (MAC): ' + data['ip_physical_addr']
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 70))

    text = 'Endereço IPV6: ' + data['ip_ipv6_addr']
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 100))
