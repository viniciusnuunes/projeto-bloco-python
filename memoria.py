import psutil
import pygame
import properties as CONSTAT

memoria_surface = pygame.surface.Surface(
    (CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA))

memoria_info = psutil.virtual_memory()


def exibeMemoriaInfo(tela, font):
    __desenha_memoria(memoria_surface, tela, font)


def __desenha_memoria(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTAT.PRETO)
    tela.blit(surface, (0, 0))

    # Desenhando a barra de memória
    largura = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 70))
    tela.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de memória
    largura = largura * memoria_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 70))
    tela.blit(surface, (0, 0))

    total = round(memoria_info.total/(1024*1024*1024), 2)

    # Desenhando o texto acima da barra de memória
    texto_barra = "Uso de Memória (Total: " + str(total) + \
        "GB) (Utilizando: " + str(memoria_info.percent) + " %):"
    text = font.render(texto_barra, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 10))
