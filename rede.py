import psutil
import pygame
import properties as CONSTANT

ip = psutil.net_if_addrs()
ip_pc = ip['Ethernet'][1][1]
ip_mascara = ip['Ethernet'][1][2]
ip_end_fisico = ip['Ethernet'][0][1]
ip_end_ipv6 = ip['Ethernet'][2][1]

rede_surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))

memoria_info = psutil.virtual_memory()

def exibeRedeInfo(tela, font):
    __desenha_rede(rede_surface, tela, font)

def __desenha_rede(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))

    # Desenhando o texto acima da barra de memória
    texto_ip = f'IP: {ip_pc}'
    text_ip = font.render(texto_ip, 1, CONSTANT.BRANCO)
    tela.blit(text_ip, (20, 10))
    texto_mascara = f'Mascara: {ip_mascara}'
    text_mascara = font.render(texto_mascara, 1, CONSTANT.BRANCO)
    tela.blit(text_mascara, (20, 40))
    texto_end_fisico = f'Endereço Físico(MAC): {ip_end_fisico}'
    text_end_fisico = font.render(texto_end_fisico, 1, CONSTANT.BRANCO)
    tela.blit(text_end_fisico, (20, 70))
    texto_end_ipv6 = f'Endereço IPV6: {ip_end_ipv6}'
    text_end_ipv6 = font.render(texto_end_ipv6, 1, CONSTANT.BRANCO)
    tela.blit(text_end_ipv6, (20, 100))
