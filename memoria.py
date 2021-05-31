import psutil
import pygame
import properties as CONSTAT

memoria_surface = pygame.surface.Surface(
    (CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA))

memoria_info = psutil.virtual_memory()


def exibeMemoriaInfo(tela, font):
    __desenha_memoria(memoria_surface, tela, font)

mem_virtual = psutil.virtual_memory()
mem_total = mem_virtual[0]
mem_uso = mem_virtual[3]
mem_livre = mem_virtual[1]
mem_percent = mem_virtual[2]
swap_mem = psutil.swap_memory()

def __desenha_memoria(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTAT.PRETO)
    tela.blit(surface, (0, 0))

    # Desenhando a barra de memória
    largura = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 30))
    tela.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de memória
    largura = largura * memoria_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 0))

    total = round(memoria_info.total/(1024*1024*1024), 2)

    # Desenhando o texto acima da barra de memória
    texto_barra = "Uso de Memória: (" + str(total) + " GB):"
    text = font.render(texto_barra, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 10))

    # Desenhando a porcentagem de uso da memoria
    largura = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 30))
    tela.blit(surface, (0, 100))

    # Desenhando a barra da porcentagem de uso da memoria
    largura = largura * memoria_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 100))

    # Total da porcentagem da memoria em uso
    texto_total = "Porcentagem de memória utilizado: (" + str(memoria_info.percent) + "%):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 100))

    # Desenhando o total de memoria em uso
    largura = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 30))
    tela.blit(surface, (0, 200))

    # Desenhando a barra de uso por cima do total de memoria em uso
    largura = largura * memoria_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 200))

    # Total de memoria em uso
    texto_total = "Total de Memória em uso: (" + str(round(mem_uso/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 200))

    # Desenhando o total de memoria livre
    largura = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura, 30))
    tela.blit(surface, (0, 300))

    # Desenhando a barra de uso por cima do total de memoria livre
    largura = largura * memoria_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 300))

    # Total de memoria livre
    texto_total = "Total de Memória Livre: (" + str(round(mem_livre/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 300))