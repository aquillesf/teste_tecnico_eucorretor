#Exercício 3: Word Ladder (Escada de Palavras)

#- Descrição: Neste exercício, você deve implementar uma função que encontra o comprimento do caminho mais curto de transformação de uma palavra inicial para uma palavra final, seguindo as regras abaixo:
  #1. A cada transformação, apenas uma letra pode ser alterada.
 # 2. Cada palavra intermediária deve existir no dicionário fornecido.
 
  #A entrada do exercício será composta por duas palavras de mesma dimensão e uma lista de palavras. Sua tarefa é encontrar a sequência mais curta de transformações, ou retornar 0 caso não seja possível.
 
#Exemplo:
#ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])  
# Saída: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")

#ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])  
# Saída: 0 (não há caminho possível)





#este problema é mais complicado, então tive que criar uma nova função que retorna uma nova string modificada

def substituir_caractere(string, indice, char):
    return string[:indice] + char + string[indice + 1:]

def escada_de_palavras(inicio, fim, dicionario):
    tabela_dicionario = {substituir_caractere(palavra, j, '?'): i 
                         for i, palavra in enumerate(dicionario) 
                         for j in range(len(palavra))}

    tabela_fim = {substituir_caractere(fim, j, '?'): j for j in range(len(fim))}
    
#função recursiva pra encontrar o caminho mais rapido para a palavras
    
    def resolver(palavra, caminho):
        for j in range(len(palavra)):
            chave = substituir_caractere(palavra, j, '?')

            if chave in tabela_fim:
                return caminho + [fim]
            
            if chave in tabela_dicionario:
                proxima = dicionario[tabela_dicionario[chave]]
                if proxima not in caminho:
                    resultado = resolver(proxima, caminho + [proxima])
                    if resultado:
                        return resultado
        return None

    return len(resolver(inicio, [inicio])) 

print(escada_de_palavras("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
