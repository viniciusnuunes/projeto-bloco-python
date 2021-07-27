import os
import pygame
import time
import properties as CONSTANT

arquivo_surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))


def exibeArquivosInfo(tela, font):
    __desenha_arquivos(arquivo_surface, tela, font)


def __desenha_arquivos(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))

    texto = 'Arquivos e Pastas (Detalhado)'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 10))

    lista_de_arquivos = os.listdir()
    dict_arquivo = {}

    for arquivo in lista_de_arquivos:
        is_file = os.path.isfile(arquivo)
        if is_file:
            dict_arquivo[arquivo] = []
            dict_arquivo[arquivo].append(os.stat(arquivo).st_size)
            dict_arquivo[arquivo].append(os.stat(arquivo).st_atime)
            dict_arquivo[arquivo].append(os.stat(arquivo).st_mtime)

    texto = '{:30}'.format("Nome")
    texto = texto + '{:11}'.format("Tamanho")
    texto = texto + '{:27}'.format("Data de Modificação")
    texto = texto + '{:27}'.format("Data de Criação")

    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 40))

    distancia_texto = 70

    for arquivo in dict_arquivo:
        kb = (dict_arquivo[arquivo][0])/1000
        tamanho = '{:10}'.format(str('{:.2f}'.format(kb)) + ' KB')
        nome_arquivo = '{:27}'.format(arquivo)

        texto = nome_arquivo + " " + tamanho + \
            time.ctime(dict_arquivo[arquivo][2]) + \
            time.ctime(dict_arquivo[arquivo][1])

        texto = font.render(texto, 1, CONSTANT.BRANCO)
        tela.blit(texto, (20, distancia_texto))
        distancia_texto += 20
