n=13
primo =1

for i in range(1,14):
    if(n%i ==0):
        print('achei',i)
        primo = 0
if (primo==1):
        print(n, 'primo')
