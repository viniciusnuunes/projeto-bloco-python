import psutil
import pygame
import properties as CONSTAT

memoria_surface = pygame.surface.Surface(
    (CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA))

memoria_info = psutil.virtual_memory()


def exibeMemoriaInfo(tela, font):
    __desenha_memoria(memoria_surface, tela, font)

mem = psutil.virtual_memory()
mem_total = mem[0]
mem_uso = mem[3]
mem_livre = mem[1]
mem_percent = mem[2]
swap_mem = psutil.swap_memory()

def __desenha_memoria(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTAT.PRETO)
    tela.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de disco
    largura = ((round(mem_total/(1024*1024*1024), 2))) - (round(mem_uso/(1024*1024*1024), 2))
    print(largura)
    largura2 = ((round(mem_total/(1024*1024*1024))))
    print(largura2)
    pygame.draw.rect(surface, CONSTAT.VERMELHO, (20, 50, largura2, 30))
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 90))

    # Desenhando o texto acima da barra de memória
    texto_barra = "Total de Memória: (" + str(round(mem_total/(1024*1024*1024), 2)) + " GB):"
    text = font.render(texto_barra, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 10))

    # Total de memoria em uso
    texto_total = "Usado: (" + str(round(mem_uso/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 40))

    # Total de memoria livre
    texto_total = "Livre: (" + str(round(mem_livre/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 70))

    # Total da porcentagem da memoria em uso
    texto_total = "Porcentagem de uso de Memória: (" + str(memoria_info.percent) + "%):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 100))