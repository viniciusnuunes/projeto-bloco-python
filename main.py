#import psutil
import pygame
import properties as CONSTANT
import cpu_cores as CpuCoreInfo
import disco as DiscoInfo
import memoria as MemoriaInfo
import rede as RedeInfo
import resumo as ResumoInfo
import arquivos_simples as ArquivoSimplesInfo
import arquivos_detalhado as ArquivoDetalhadoInfo
import pid as PidInfo

PID = CONSTANT.PID

# Inicialização da tela e fonte
pygame.font.init()
pygame.display.init()

lista_telas = [0, 1, 2, 3, 4, 5, 6, 7]

# Definições da tela, fonte e título da janela
tela = pygame.display.set_mode((CONSTANT.LARGURA_TELA, CONSTANT.ALTURA_TELA))
lista_fontes = pygame.font.get_fonts()

if 'calibri' in lista_fontes:
    fonte = 'calibri'
else:
    fonte = None

font = pygame.font.SysFont(fonte, 24)
pygame.display.set_caption('Gerenciador de tarefas')

clock = pygame.time.Clock()
count = 30

finalizado = False

tela_atual = lista_telas[0]

while not finalizado:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizado = True

        if count == 30:
            if tela_atual == 0:
                CpuCoreInfo.exibeCpuCoreInfo(tela, font)
                count = 0

            if tela_atual == 1:
                DiscoInfo.exibeDiscoInfo(tela, font)
                count = 0

            if tela_atual == 2:
                MemoriaInfo.exibeMemoriaInfo(tela, font)
                cout = 0

            if tela_atual == 3:
                RedeInfo.exibeRedeInfo(tela, font)
                count = 0

            if tela_atual == 4:
                ResumoInfo.exibeResumoInfo(tela, font)
                count = 0
            
            if tela_atual == 5:
                ArquivoSimplesInfo.exibeArquivosInfo(tela, font)
                count = 0
                
            if tela_atual == 6:
                ArquivoDetalhadoInfo.exibeArquivosInfo(tela, font)
                count = 0
                
            if tela_atual == 7:
                PidInfo.exibePidInfo(tela, font, PID)
                count = 0
                


        if event.type == pygame.KEYDOWN:
            count = 29
            if event.key == pygame.K_LEFT:
                proxima_tela = lista_telas[tela_atual] - 1

                if proxima_tela < 0:
                    print('Não tem mais tela pra esquerda')
                    continue

                tela_atual = proxima_tela

            if event.key == pygame.K_RIGHT:
                proxima_tela = lista_telas[tela_atual] + 1

                if proxima_tela > 7:
                    print('Não tem mais tela pra direita')
                    continue

                tela_atual = proxima_tela

            if event.key == pygame.K_SPACE:
                proxima_tela = 4
                print('Vou para a tela TODOS')

                tela_atual = proxima_tela
                
            if event.key == pygame.K_F5 and tela_atual == 7:
                PID = CONSTANT.geraPid()
                print('PID Atualizado com sucesso...')
                PidInfo.exibePidInfo(tela, font, PID)

        pygame.display.update()

        clock.tick(30)
        count += 1

pygame.display.quit()
