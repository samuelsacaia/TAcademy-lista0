
def mostrar_o_resultado(ano) ->None:
    if(ano %4==0 and ano%100!=0) or (ano%400==0):
        print('bissexto')
    else:
        print('não bissexto')
        print(f'{ano}')




        #Resposta: o ano bissexto é considerado quando é dividido por 4(quatro) e não só ,
        #não pode ser dividido por 100(cem) e se o ano for divido por 400 tanbem é ano bissexto