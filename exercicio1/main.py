
from src.Application.input import pegar_lista
from src.Application.domain import soma_numero,mult_numero,numeros_primos

if __name__== '__main__':
  lista_numero = pegar_lista()
  soma=soma_numero(lista_numero)
  multiplicacao = mult_numero( lista_numero)
  #impare = numeros_impares(lista_numero)
  primos = numeros_primos(multiplicacao)
  print(primos)



  #mult = mult_numero(soma)
  


