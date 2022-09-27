def numeros_primos(lista_numero):
    lista_primos=[]
    for numero in lista_numero:
        if numero%2==0:

        #if e_primo(numero):    
            lista_primos.append(numero)
            quantidade=len(lista_numero)
            if quantidade>2:
                return lista_primos
        else:
            return lista_primos
           

    return lista_primos






   
def pegar_lista()-> list[int]:
    lista_numero=[]
    for i in range(7):
        valor = str(input('digite os numero'))
        lista_numero.append(int(valor))
    return lista_numero



