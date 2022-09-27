from src.application.input import pega_ano
from src.application.output import mostra_mensagem


def e_bissexto(ano: int):
    if(ano%4==0 and ano%100!=0) or (ano%400==0):
        return True
        return False

if __name__ =='__main__':
  ano = pega_ano()

  if e_bissexto(ano):
        mostra_mensagem('bissexto')
  else:
        mostra_mensagem(f'não bissexto')