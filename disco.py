import pygame
import properties as CONSTANT

disco_surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))



def exibeDiscoInfo(tela, font, data):
    __desenha_uso_hd(disco_surface, tela, font, data)





def __desenha_uso_hd(surface, tela, font, data):
    print(data)
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de disco
    largura = CONSTANT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTANT.CINZA, (20, 50, largura, 30))
    tela.blit(surface, (0, 90))
    
    largura = largura * data['disk_percent'] / 100
    pygame.draw.rect(surface, CONSTANT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 90))

    # Capacidade total do disco
    texto_total = "Total do Disco: (" + \
        str(round(data['disk_total']/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 10))

    # Desenhando o texto acima da barra de uso de disco
    texto_barra = "Usado: (" + str(data['disk_percent'])+" %):"
    text = font.render(texto_barra, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 40))

    # Espaço livre do disco
    texto_livre = "Livre: (" + str(round(data['disk_free'] /
                                         (1024*1024*1024), 2))+" GB):"
    text = font.render(texto_livre, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 70))

    # Porcentagem de uso do disco
    texto_barra = "Porcentagem de uso de Disco: (" + \
        str(data['disk_percent'])+" %):"
    text = font.render(texto_barra, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 100))
