import psutil
import pygame
import properties as CONSTAT

disco_surface = pygame.surface.Surface(
    (CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA))

disco_info = psutil.disk_usage('.')

def exibeDiscoInfo(tela, font):
    __desenha_uso_hd(disco_surface, tela, font)

###
disk = psutil.disk_usage('/')
disk_total = disk[0]
disk_uso = disk[1]
disk_livre = disk[2]
disk_porcentagem = disk[3]
###

def __desenha_uso_hd(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTAT.PRETO)
    tela.blit(surface, (0, 0))
    
    # Desenhando a barra de disco
    largura = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 30))
    tela.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de disco
    largura = largura * disco_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 0))

    # Desenhando o texto acima da barra de uso de disco
    texto_barra = "Porcentagem de uso de Disco: (" + str(disco_info.percent)+" %):"
    text = font.render(texto_barra, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 10))

    # Desenhando o total de disco
    largura = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 30))
    tela.blit(surface, (0, 100))

    # Desenhando a barra de uso por cima do total de disco
    largura = largura * disco_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 100))

    # Total de disco
    texto_total = "Total de Disco: (" + str(round(disk_total/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 100))

     # Desenhando o uso de disco
    largura = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 30))
    tela.blit(surface, (0, 200))

    # Desenhando a barra de uso por cima do uso de disco
    largura = largura * disco_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 200))

    # Uso de disco
    texto_uso = "Uso de Disco: (" + str(round(disk_uso/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_uso, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 200))


     # Desenhando o espaço livre de disco
    largura = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 30))
    tela.blit(surface, (0, 300))

    # Desenhando a barra de uso por cima do espaço livre de disco
    largura = largura * disco_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 300))

    # Espaço livre do disco
    texto_livre = "Espaço livre no Disco: (" + str(round(disk_livre/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_livre, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 300))