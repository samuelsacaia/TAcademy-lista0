#2- Atende cliente: Retira da lista o último cliente adicionado
#c.3Fim
"""""
def delete(lista,valor):

    if valor == 1:
        nome = 'Pilha'
        lista.pop(nome)
    return lista
    """


def delete(list,valor):
    while (True):
       if(valor == '1'):
           nome = 'Pilha'
           list.pop(nome)
           return nome


def controller(list,valor):
   if(valor == '1'):
    return delete(list,valor)

 