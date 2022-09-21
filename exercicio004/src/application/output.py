
def mostrar_o_resultado(ano) ->None:
    if(ano %4==0 and ano%100!=0) or (ano%400==0):
        print('bissexto')
    else:
        print('não bissexto')
        print(f'{ano}')