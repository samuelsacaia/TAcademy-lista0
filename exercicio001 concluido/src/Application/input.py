#1 - Faça um progrma que leia N numeros inteiros e joga em uma lista de numeros.

def pegar_lista()-> list[int]:
    lista_numero=[]
    for i in range(7):
        valor = str(input('digite os numero'))
        lista_numero.append(int(valor))
    return lista_numero



