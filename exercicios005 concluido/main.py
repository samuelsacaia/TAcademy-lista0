
    
from src.application.output import mostra_menu
from src.application.input import adicionar_cliente, pegar_opcao


if __name__ == '__main__':
   lista_cliente=[]

   while True:
      mostra_menu()
      opcao=pegar_opcao()
      if(opcao==3):
         print('Fim!...')
         break

      elif(opcao==1):
        cliente=adicionar_cliente()
        lista_cliente.append(cliente)
        print(f'cliente aguardando.{lista_cliente}')

      elif(opcao==2 and len(lista_cliente)>0 ): 
         cliente_chamado=lista_cliente.pop(0)
         print(f'cliente chamado:{cliente_chamado}')

      else:
         print(f'não há cliente na fila.')

     
      

