


#A-SOMA:
from itertools import count


def soma_numero(lista_numero ):
    soma = sum(lista_numero)
    return soma

#B-MULTIPLICAÇÃO:
def mult_numero(lista_numero):
    multiplicacao = lista_numero[0]
    for i in range(1, len(lista_numero)):
        multiplicacao = multiplicacao * lista_numero[i]

    return multiplicacao

#C-DUPLICADOS:
def pega_duplicados(lista_numero):
    numeros_duplicados = []
    copia_lista = lista_numero.copy()

    for numero in lista_numero:
        repeticoes = copia_lista.count(numero)
        if repeticoes > 1:
            numeros_duplicados.append(numero)
            while numero in copia_lista:
                copia_lista.remove(numero)

    return numeros_duplicados
    

#D-IMPARES:

def numeros_impares(lista_numero):
    lista_impares = []
              
    for numero in lista_numero:
        if numero%2 != 0:
            lista_impares.append(numero)

    return lista_impares


#E-PARES:
def numeros_pares(lista_numeros):
    lista_pares = []
    for i in range(len(lista_numeros)):
        if ((lista_numeros[i]%2)==0):
            lista_pares.append(lista_numeros[i])
    return lista_pares        

#F-NUMEROS PRIMOS:
def numeros_primos(lista_numero):
    lista_primos=[]
    for numero in lista_numero:
        if numero%2==0:
            lista_primos.append(numero)
            quantidade=len(lista_numero)
            if quantidade>2:
                return lista_primos
        else:
            return lista_primos


   






   
    
      
   


 




  






