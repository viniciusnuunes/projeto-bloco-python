import cpu as CpuInfo
import properties as CONSTANT


tamanho_altura_por_info = CONSTANT.ALTURA_TELA / 4

altura_cpu = tamanho_altura_por_info
altura_disco = tamanho_altura_por_info * 2
altura_memoria = tamanho_altura_por_info * 3
altura_rede = tamanho_altura_por_info * 4

def exibeInformacoesResumidas(tela, font):    
    CpuInfo.exibeCpuTodas(tela, font, 0, altura_cpu)
