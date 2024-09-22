import random

def crossover(pai1, pai2, pontos_de_corte=1):
    if pontos_de_corte == 1:
        ponto = random.randint(1, len(pai1) - 1)
        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]
    else:
        ponto1 = random.randint(1, len(pai1) - 2)
        ponto2 = random.randint(ponto1, len(pai1) - 1)
        filho1 = pai1[:ponto1] + pai2[ponto1:ponto2] + pai1[ponto2:]
        filho2 = pai2[:ponto1] + pai1[ponto1:ponto2] + pai2[ponto2:]
    return filho1, filho2
