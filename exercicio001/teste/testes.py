'''''
def nprimo(lista_numero):
    primos=[]
    for i in range(1,lista_numero+1):
        if lista_numero%i ==0:
            primos.append(i)
    return primos
print(nprimo(10))
'''

#def numeros_pares(lista_numeros):
 #   pares = list([])
 #   for i in range(len(lista_numeros)):
   #     if ((lista_numeros[i]%2)==0):
   #         pares.append(lista_numeros[i])
  #  return pares        


def numeros_impares(lista_numero):
    impares=list([])
    for i in range(len(lista_numero-1)):
      if((lista_numero[i]%3)==0):
            impares.append(lista_numero[i])
    print(impares)       