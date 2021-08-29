import psutil
import os
import random
import pygame
import time
import properties as CONSTANT


pid_surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))


def exibePidInfo(tela, font, pid):
    __desenha_pid(pid_surface, tela, font, pid)


def __desenha_pid(surface, tela, font, pid):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))

    texto = 'Informações do PID'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 10))

    texto = f'Nome: {pid.name()}'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 50))

    texto = f'Executável: {pid.exe()}'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 80))

    texto = f'Tempo de criação: {time.ctime(pid.create_time())}'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 110))

    texto = f'Tempo de usuário: {pid.cpu_times().user}s'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 140))

    texto = f'Tempo de sistema: {pid.cpu_times().system}s'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 170))

    texto = f'Tempo de sistema: {pid.cpu_percent(interval = 1.0)}%'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 200))

    perc_mem = "{:.2f}".format(pid.memory_percent())
    texto = f'Percentual de uso de memória: {perc_mem}%'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 230))

    mem = "{:.2f}".format(pid.memory_info().rss/1024/1024)
    texto = f'Uso de memória: {mem}MB'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 260))

    texto = f'Número de threads: {pid.num_threads()}'
    texto = font.render(texto, 1, CONSTANT.BRANCO)
    tela.blit(texto, (20, 290))
