import pygame
import properties as CONSTANT


surface = pygame.surface.Surface(
    (CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))


def exibePidInfo(tela, font, data):
    surface.fill(CONSTANT.PRETO)
    tela.blit(surface, (0, 0))

    text = 'Informações do PID'
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 10))

    text = 'Nome: ' + data['pid_name']
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 50))

    text = 'Executável: ' + data['pid_exe']
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 80))

    text = 'Tempo de criação: ' + data['pid_date_creation']
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 110))

    text = 'Tempo de usuário: ' + str(data['pid_user_time'])
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 140))

    text = 'Tempo de sistema: ' + str(data['pid_system_time'])
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 170))

    text = 'Tempo de sistema: ' + str(data['pid_system_percent']) + '%'
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 200))

    text = 'Percentual de uso de memória: ' +  str(round(data['pid_memory_percent'], 2)) + '%'
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 230))

    pidMemoryUse = data['pid_memory_use']
    pidMemoryUse = str(round((pidMemoryUse / 1024 / 1024), 2))
    text = 'Uso de memória: ' + pidMemoryUse + 'MB'
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 260))

    text = 'Número de threads: ' + str(data['pid_threads'])
    text = font.render(text, 1, CONSTANT.BRANCO)
    tela.blit(text, (20, 290))
