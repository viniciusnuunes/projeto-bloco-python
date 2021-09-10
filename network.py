import pygame
import properties as CONSTANT

surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))


def exibeRedeInfo(tela, font, data):
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))

    text = 'IP: ' + data['ip_pc']
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 10))

    text = 'Mascara: ' + data['ip_mask']
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 40))

    text = 'Endereço Físico (MAC): ' + data['ip_physical_addr']
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 70))

    text = 'Endereço IPV6: ' + data['ip_ipv6_addr']
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 100))
