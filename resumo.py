#import psutil
import pygame
import cpuinfo
import sys
import platform
import psutil
import pygame
import properties as CONSTAT
import cpu_cores as CpuCoreInfo
import disco as DiscoInfo
import memoria as MemoriaInfo
import rede as RedeInfo
import resumo as ResumoInfo

resumo_surface = pygame.surface.Surface(
    (CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA))

memoria_info = psutil.virtual_memory()

ip = psutil.net_if_addrs()
ip_pc = ip['Ethernet'][1][1]

disk = psutil.disk_usage('/')
disk_total = disk[0]

mem = psutil.virtual_memory()
mem_total = mem[0]
mem_uso = mem[3]

cpu_info = cpuinfo.get_cpu_info()
nome_cpu = cpu_info['brand_raw']


def exibeResumoInfo(tela, font):
    __desenha_resumo(resumo_surface, tela, font)


def __desenha_resumo(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTAT.PRETO)
    tela.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de disco
    largura = (CONSTAT.LARGURA_TELA - 2 * 20) - int(disk.percent)
    largura2 = (CONSTAT.LARGURA_TELA - 2 * 20)
    pygame.draw.rect(surface, CONSTAT.CINZA, (20, 50, largura2, 30))
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 60))

    # Desenhando o texto acima da barra de memória
    texto_ip = f'CPU: {nome_cpu}'
    text_ip = font.render(texto_ip, 1, CONSTAT.BRANCO)
    tela.blit(text_ip, (20, 10))

    # Desenhando o texto acima da barra de memória
    texto_ip = f'IP: {ip_pc}'
    text_ip = font.render(texto_ip, 1, CONSTAT.BRANCO)
    tela.blit(text_ip, (20, 40))

    # Capacidade total do disco
    texto_total = "Total do Disco: (" + \
        str(round(disk_total/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 70))

    # desenhando a barra
    largura = ((round(mem_total/(1024*1024*1024), 2))) - \
        (round(mem_uso/(1024*1024*1024), 2))
    largura_total = CONSTAT.LARGURA_TELA - 2 * 20
    pygame.draw.rect(surface, CONSTAT.CINZA, (20, 50, largura_total, 30))
    tela.blit(surface, (0, 200))

    # desenhando a barra de uso
    largura = largura_total * memoria_info.percent / 100
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 150))

    # Total de memoria em uso
    texto_total = "Memória em Uso: (" + \
        str(round(mem_uso/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 160))
