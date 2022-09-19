
from src.Application.output import mostra_o_resultado
from src.Application.input import pegar_lista
from src.Application.domain import soma_numero,mult_numero,pega_duplicados,numeros_impares,numeros_pares,numeros_primos

if __name__=='__main__':
    lista_numero=pegar_lista()
    soma = soma_numero(lista_numero)
    multiplicacao = mult_numero(lista_numero)
    numeros_duplicados = pega_duplicados(lista_numero)
    lista_impares=numeros_impares(lista_numero)
    lista_pares =numeros_pares(lista_numero)
    lista_primos=numeros_primos(lista_numero)
  
    mostra_o_resultado(lista_numero,soma,multiplicacao,numeros_duplicados,lista_impares,lista_pares,lista_primos)
  
    
   