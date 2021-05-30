import psutil
import pygame
import properties as CONSTAT

ip = psutil.net_if_addrs()
ip_pc = ip['Ethernet'][1][1]
ip_mascara = ip['Ethernet'][1][2]
ip_end_fisico = ip['Ethernet'][0][1]
ip_end_ipv6 = ip['Ethernet'][2][1]

network_surface = pygame.surface.Surface(
    (CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA))

memoria_info = psutil.virtual_memory()


def exibeNetworkInfo(tela, font):
    __desenha_network(network_surface, tela, font)


def __desenha_network(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTAT.PRETO)
    tela.blit(surface, (0, 0))

    # Desenhando o texto acima da barra de memória
    texto_ip = f'IP: {ip_pc}'
    text_ip = font.render(texto_ip, 1, CONSTAT.BRANCO)
    tela.blit(text_ip, (20, 0))
    texto_mascara = f'Mascara: {ip_mascara}'
    text_mascara = font.render(texto_mascara, 1, CONSTAT.BRANCO)
    tela.blit(text_mascara, (20, 25))
    texto_end_fisico = f'Endereço Físico(MAC): {ip_end_fisico}'
    text_end_fisico = font.render(texto_end_fisico, 1, CONSTAT.BRANCO)
    tela.blit(text_end_fisico, (20, 50))
    texto_end_ipv6 = f'Endereço IPV6: {ip_end_ipv6}'
    text_end_ipv6 = font.render(texto_end_ipv6, 1, CONSTAT.BRANCO)
    tela.blit(text_end_ipv6, (20, 75))
