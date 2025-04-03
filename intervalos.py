#Exercício 2: Mesclar Intervalos

#- Descrição: Dada uma lista de intervalos, você deve implementar uma função que mescla os intervalos sobrepostos.
#Cada intervalo é representado por um par de números [início, fim]. Caso dois intervalos se sobreponham,
#eles devem ser combinados em um único intervalo.

#Exemplo:
#merge_intervals([[1,3], [2,6], [8,10], [15,18]])  
# Saída: [[1, 6], [8, 10], [15, 18]]

#merge_intervals([[1,4], [4,5]])  
# Saída: [[1, 5]]

def merge_intervals(intervalos):
    
    #Nesse exercício eu ordenei as listas  e percorri os intervalos verificando as sobreposições e adicionando os intervalos mesclados na "resposta"
    
    intervalos.sort()
    resposta = [intervalos[0]]
    
    for x, y in intervalos[1:]:
        
        if resposta[-1][1] < x:
            resposta.append([x, y])
        else:
            resposta[-1][1] = max(resposta[-1][1], y)
    return print(resposta)

merge_intervals([[1,3], [2,6], [8,10], [15,18]])
