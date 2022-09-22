#Faça um programa que funciona como uma fila de banco. É necessario
#um menu com 3 opçôes:

#a.1- Adicionar cliente: Recebe um nome e adiciona na lista
#b.2- Atende cliente: Retira da lista o proximo a ser atendido.
#c.3- Fim

def adicionar():
    lista=[]
    cliente =int(input('Digite o nome:'))
    lista.append(cliente)
    return lista
