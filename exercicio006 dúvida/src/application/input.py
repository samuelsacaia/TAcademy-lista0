# Faça um programa que funcione como uma pilha.É necessario um menu com 3 opções:
#a. 1- Adicionar cliente: Recebe um nome e diciona na lista.
#b. 2- Atende cliente: Retira da lista o último cliente adicionado
#c. 3-Fim

"""""
#def adicionar()->list:
    while True:
        lista =[]
        cliente = int(input('Digite o nome'))
        lista.append(cliente)
    return  lista
    """
from http import client


def adicionar(list):
    cliente = str(input('Digite o nome: '))
    list.append(cliente)
    return client


