#Faça um programa que leia N números inteiros e os jogue em uma lista de números.lista
# Apos isso, faça as seguintes rotinas:
# a.Soma:Recebe a lista de números com parâmetro e retorna a soma .
# b.Multiplica: Recebe a lista de numero como parâmetro e retorna a multiplicacao dos numeros.
# c. Duplicados: Recebe a lista de números como parâmetro e retorna uma lista com os
#numeros Queue aparecem mais de uma vez.
#d. Impares: Recebe a lista de numeros como parâmetro e retorna uma lista com numeros impares.
#e. Pares: Recebe a lista de numeros como parâmetro e retorna uma lista com numeros pares.
#f. Primos: Recebe a lista de numeros como parâmetro e retorna uma lista com numeros Primos.


def pegar_lista()-> list[int]:
    lista_numero=[]
    while True:
        valor = int(input('Digite um numero: [Zero para Terminar] '))
        if (valor == 0):
            break
        
        lista_numero.append(valor)
    
    return lista_numero
