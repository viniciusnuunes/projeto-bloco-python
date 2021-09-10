import pygame
import time
import properties as CONSTANT

surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))


def exibeArquivosInfo(tela, font, data):
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))

    text = 'Arquivos e Pastas (Detalhado)'
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 10))

    text = '{:30}'.format("Nome")
    text = text + '{:11}'.format("Tamanho")
    text = text + '{:27}'.format("Data de Modificação")
    text = text + '{:27}'.format("Data de Criação")

    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 40))

    distancia_texto = 70

    for file in data:
        kb = (data[file][0])/1000
        tamanho = '{:10}'.format(str('{:.2f}'.format(kb)) + ' KB')
        nome_arquivo = '{:27}'.format(file)

        text = nome_arquivo + " " + tamanho + \
            time.ctime(data[file][2]) + \
            time.ctime(data[file][1])

        text = font.render(text, 1, CONSTANT.BRANCO)
        tela.blit(text, (20, distancia_texto))
        distancia_texto += 20
