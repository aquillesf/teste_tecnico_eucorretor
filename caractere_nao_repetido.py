
#- Descrição: Neste exercício, você deve implementar uma função que encontra o primeiro caractere que não se repete em uma string.
#Caso todos os caracteres sejam repetidos, a função deve retornar -1.
 
#Exemplo:
#firstUniqChar("abacabad")  # Saída: 3 ('c')
#firstUniqChar("aaabb")      # Saída: -1 (não há caracteres não repetidos)


def firstUniqChar(string):
    
    #Olá! tudo bem?
    #Para este problema, eu consigo resolver ele de duas formas bem rápidas e simples, ou eu uso a função
    #embutida no python (o Counter), ou eu posso também transformar em um dicionário que remove todos os
    #caracteres repetidos, mas como esse é um teste de raciocínio lógico, vou fazer de uma forma mais "manual" e percorrer a lista com 2 for loops
    
    lista_string = " ".join(string).split()
    tamanho_str = len(lista_string)
    char_unicos = []
    
    for i in range(0, tamanho_str):
        contador = 0
        str_atual = lista_string[i]
        
        for y in range(0, tamanho_str):
            if str_atual == lista_string[y]:
                contador += 1
                
            if y == tamanho_str -1 and contador == 1:
                char_unicos.append(str_atual)
                
    
    if len(char_unicos) == 0:
        return print("-1")
    
    print(*char_unicos[0])
                


firstUniqChar("aaabb")