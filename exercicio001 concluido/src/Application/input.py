#1 - Faça um progrma que leia N numeros inteiros e joga em uma lista de numeros.

def pegar_lista()-> list[int]:
    lista_numero=[]
    while True:
        valor = int(input('Digite um numero: [Zero para Terminar] '))
        if (valor == 0):
            break
        
        lista_numero.append(valor)
    
    return lista_numero



