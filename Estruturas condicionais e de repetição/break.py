while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10:
        break
    
    print(numero)
    
for numero2 in range(100):
    
    if numero2 % 3 == 0:
       continue
    
    print(numero2)