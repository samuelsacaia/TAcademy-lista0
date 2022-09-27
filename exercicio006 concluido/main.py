    
from src.application.output import mostra_menu
from src.application.input import adicionar_cliente, pegar_opcao


if __name__ =='__main__':
   lista_cliente=[]
   
   while True:
      mostra_menu()
      opcao=pegar_opcao()
      if(opcao==3):
         print('Fim')
         break

      elif(opcao==1):
         cliente1=adicionar_cliente()
         lista_cliente.append(cliente1)
         print(f'cliente aguardar:{lista_cliente}')


      elif(opcao==2):
         cliente2=lista_cliente.pop()
         print(f'cliente chamado:{lista_cliente}')

    



