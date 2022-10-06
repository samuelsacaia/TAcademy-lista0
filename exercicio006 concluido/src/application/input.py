#6- Faça um programa que funcione como uma pilha. É necessario um menu com 3 opcao:
#a.1- Adicionar cliente. Receber um nome e adicionar na lista
#a.2-Atendente cliente: Retira da lista o ultimo cliente adicionado.
#c.3-Fim


def adicionar_cliente():
    cliente= str(input('Digite o nome:'))
    return cliente

def pegar_opcao():
    opcao =int(input('Escolher a opcao:'))
    return opcao