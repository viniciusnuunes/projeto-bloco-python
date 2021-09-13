import pygame
import properties as CONSTANT

surface = pygame.surface.Surface(
    (CONSTANT.SCREEN_WIDTH, CONSTANT.SCREEN_HEIGHT))


def drawNetwork(screen, font, data, hosts):    
    surface.fill(CONSTANT.BLACK)
    screen.blit(surface, (0, 0))

    text = 'Informações da Rede'
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 10))
    
    text = 'IP: ' + data['ip_pc']
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (50, 40))

    text = 'Mascara: ' + data['ip_mask']
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (50, 70))

    text = 'Endereço Físico (MAC): ' + data['ip_physical_addr']
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (50, 100))

    text = 'Endereço IPV6: ' + data['ip_ipv6_addr']
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (50, 130))

    text = 'Informações dos Hosts'
    text = font.render(text, 1, CONSTANT.WHITE)
    screen.blit(text, (20, 160))
    
    initialWidth = 190
    
    hostNames = hosts['hostsNames']
    hostPorts = hosts['hostsPorts']
    
    for host in hostNames:        
        text = 'Host: ' + host + ' - ' + hostNames[host]
        text = font.render(text, 1, CONSTANT.WHITE)
        screen.blit(text, (50, initialWidth))
        initialWidth += 20
        
    print('Exibindo o estado das portas dos Hosts no terminal')
    print(hostPorts)