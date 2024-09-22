import random

def selecao_por_torneio(populacao, fitness_populacao, tamanho_torneio=3):
    torneio = random.sample(list(zip(populacao, fitness_populacao)), tamanho_torneio)
    return max(torneio, key=lambda x: x[1])[0]
