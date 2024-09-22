from algoritmo_genetico import algoritmo_genetico

limites = [-10, 10]
tamanho_populacao = 10
geracoes = 100
tamanho_cromossomo = 32
taxa_mutacao = 0.01
pontos_de_corte = 1
elitismo = True
percentual_elitismo = 0.2

melhor_x, melhor_valor = algoritmo_genetico(
    limites, 
    tamanho_populacao=tamanho_populacao, 
    geracoes=geracoes, 
    tamanho_cromossomo=tamanho_cromossomo, 
    taxa_mutacao=taxa_mutacao, 
    pontos_de_corte=pontos_de_corte, 
    elitismo=elitismo, 
    percentual_elitismo=percentual_elitismo
)

print(f"\nMelhor valor encontrado: f({melhor_x}) = {melhor_valor}")
