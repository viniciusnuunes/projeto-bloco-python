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
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 70))
    tela.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de disco
    largura = largura * disco_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 70))
    tela.blit(surface, (0, 0))

    # Desenhando o texto acima da barra de uso de disco
    texto_barra = "Uso de Disco: (" + str(disco_info.percent)+" %):"
    text = font.render(texto_barra, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 10))

    # Total de disco
    texto_total = "Total de Disco: (" + str(round(disk_total/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 150))

    # Uso de disco
    texto_uso = "Uso de Disco: (" + str(round(disk_uso/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_uso, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 170))