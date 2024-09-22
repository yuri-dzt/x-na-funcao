from funcoes import funcao_objetivo
from cromossomos import binario_para_real

def calcular_fitness(populacao, limites):
    return [1 / (1 + funcao_objetivo(binario_para_real(cromossomo, limites))) for cromossomo in populacao]
