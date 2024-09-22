import numpy as np
from fitness import calcular_fitness
from selecao import selecao_por_torneio
from crossover import crossover
from mutacao import mutacao
from cromossomos import gerar_populacao, binario_para_real
from funcoes import funcao_objetivo

def algoritmo_genetico(
    limites, 
    tamanho_populacao=10, 
    geracoes=100, 
    tamanho_cromossomo=32,
    taxa_mutacao=0.01, 
    pontos_de_corte=1, 
    elitismo=False, 
    percentual_elitismo=0.1
):
    populacao = gerar_populacao(tamanho_populacao, tamanho_cromossomo)
    
    for geracao in range(geracoes):
        fitness_populacao = calcular_fitness(populacao, limites)
        
        nova_populacao = []
        
        if elitismo:
            num_elite = int(percentual_elitismo * tamanho_populacao)
            elite = [populacao[i] for i in np.argsort(fitness_populacao)[-num_elite:]]
            nova_populacao.extend(elite)

        while len(nova_populacao) < tamanho_populacao:
            pai1 = selecao_por_torneio(populacao, fitness_populacao)
            pai2 = selecao_por_torneio(populacao, fitness_populacao)
                
            filho1, filho2 = crossover(pai1, pai2, pontos_de_corte)
            filho1 = mutacao(filho1, taxa_mutacao)
            filho2 = mutacao(filho2, taxa_mutacao)
            nova_populacao.extend([filho1, filho2])
        
        populacao = nova_populacao[:tamanho_populacao]
        
        melhores_fitness = max(fitness_populacao)
        melhor_cromossomo = populacao[fitness_populacao.index(melhores_fitness)]
        melhor_x = binario_para_real(melhor_cromossomo, limites)
        melhor_x = round(melhor_x, 2) 
        melhor_valor = round(funcao_objetivo(melhor_x), 2)  
        
        print(f"Geração {geracao+1} - Melhor valor de f(x): {melhor_valor} com x = {melhor_x}")
    
    fitness_final = calcular_fitness(populacao, limites)
    melhor_cromossomo = populacao[fitness_final.index(max(fitness_final))]
    melhor_x = binario_para_real(melhor_cromossomo, limites)
    melhor_x = round(melhor_x, 2)  
    melhor_valor = round(funcao_objetivo(melhor_x), 2) 
    return melhor_x, melhor_valor
