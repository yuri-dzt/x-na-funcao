import random

def binario_para_real(cromossomo, limites):
    cromossomo_str = ''.join(str(bit) for bit in cromossomo)
    valor_decimal = int(cromossomo_str, 2)
    tamanho_intervalo = limites[1] - limites[0]
    valor_real = limites[0] + (valor_decimal / (2**len(cromossomo) - 1)) * tamanho_intervalo
    return valor_real

def gerar_cromossomo(tamanho):
    return [random.randint(0, 1) for _ in range(tamanho)]

def gerar_populacao(tamanho_populacao, tamanho_cromossomo):
    return [gerar_cromossomo(tamanho_cromossomo) for _ in range(tamanho_populacao)]
