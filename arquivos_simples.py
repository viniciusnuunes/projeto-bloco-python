import os
import pygame
import properties as CONSTANT

arquivo_surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))


def exibeArquivosInfo(tela, font):
    __desenha_arquivos(arquivo_surface, tela, font)


def __desenha_arquivos(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))

    texto = 'Arquivos e Pastas (Simples)'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 10))

    arquivos = os.listdir()
    distancia_texto = 40

    for arquivo in arquivos:
        texto = font.render(arquivo, 1, CONSTANT.BRANCO)
        tela.blit(texto, (20, distancia_texto))
        distancia_texto += 20
