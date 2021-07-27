import psutil
import pygame
import properties as CONSTANT

disco_surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))

disco_info = psutil.disk_usage('.')


def exibeDiscoInfo(tela, font):
    __desenha_uso_hd(disco_surface, tela, font)


disk = psutil.disk_usage('/')
disk_total = disk[0]
disk_uso = disk[1]
disk_livre = disk[2]
disk_porcentagem = disk[3]


def __desenha_uso_hd(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de disco
    largura = CONSTANT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTANT.CINZA, (20, 50, largura, 30))
    tela.blit(surface, (0, 90))
    
    largura = largura * disco_info.percent / 100
    pygame.draw.rect(surface, CONSTANT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 90))

    # Capacidade total do disco
    texto_total = "Total do Disco: (" + \
        str(round(disk_total/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 10))

    # Desenhando o texto acima da barra de uso de disco
    texto_barra = "Usado: (" + str(disco_info.percent)+" %):"
    text = font.render(texto_barra, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 40))

    # Espaço livre do disco
    texto_livre = "Livre: (" + str(round(disk_livre /
                                         (1024*1024*1024), 2))+" GB):"
    text = font.render(texto_livre, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 70))

    # Porcentagem de uso do disco
    texto_barra = "Porcentagem de uso de Disco: (" + \
        str(disco_info.percent)+" %):"
    text = font.render(texto_barra, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 100))
