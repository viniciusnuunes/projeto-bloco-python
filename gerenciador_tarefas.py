#import psutil
import pygame
import sys
import platform
import psutil
import cpuinfo

cpu_info = cpuinfo.get_cpu_info()


pygame.font.init()
pygame.display.init()

preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (100, 100, 100)
vermelho = (255, 0, 0)
azul = (0, 0, 255)

largura_tela = 800
altura_tela = 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
font = pygame.font.Font(None, 28)
pygame.display.set_caption('Gerenciador de tarefas')

menu_surface = pygame.surface.Surface((largura_tela, altura_tela / 5))
display_infos_surface = pygame.surface.Surface(
    (largura_tela, (altura_tela / 5) * 4))

clock = pygame.time.Clock()
count = 60

# FUNÇÕES


def mostra_info_cpu():
    menu_surface.fill(branco)
    mostra_texto(menu_surface, "Nome:", "brand_raw", 10)
    mostra_texto(menu_surface, "Arquitetura:", "arch", 30)
    mostra_texto(menu_surface, "Palavra (bits):", "bits", 50)
    mostra_texto(menu_surface, "Frequência (MHz):", "freq", 70)
    mostra_texto(menu_surface, "Núcleos (físicos):", "nucleos", 90)
    tela.blit(menu_surface, (0, 0))


def mostra_texto(surface, nome, chave, pos_y):
    text = font.render(nome, True, preto)
    surface.blit(text, (10, pos_y))

    if chave == "freq":
        textInfo = str(round(psutil.cpu_freq().current, 2))
    elif chave == "nucleos":
        textInfo = str(psutil.cpu_count())
        textInfo = textInfo + " (" + str(psutil.cpu_count(logical=False)) + ")"
    else:
        # print(info_cpu)
        textInfo = str(cpu_info[chave])

    text = font.render(textInfo, True, cinza)
    surface.blit(text, (200, pos_y))


def mostra_uso_cpu():
    cpu_percent = psutil.cpu_percent(interval=0, percpu=True)
    display_infos_surface.fill(cinza)

    num_cpu = len(cpu_percent)
    x = y = 10
    desl = 10
    alt = display_infos_surface.get_height() - 2*y
    larg = (display_infos_surface.get_width()-2*y - (num_cpu+1)*desl)/num_cpu
    d = x + desl

    for i in cpu_percent:
        pygame.draw.rect(display_infos_surface, vermelho, (d, y, larg, alt))
        pygame.draw.rect(display_infos_surface, azul, 	(d, y, larg, (1-i/100)*alt))
        d = d + larg + desl
    # parte mais abaixo da tela e à esquerda
    tela.blit(display_infos_surface, (0, altura_tela/5))


finalizado = False

while not finalizado: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizado = True

        if count == 60:
            mostra_info_cpu()
            mostra_uso_cpu()
            count = 0

        pygame.display.update()

        clock.tick(60)
        count += 1

pygame.display.quit()
