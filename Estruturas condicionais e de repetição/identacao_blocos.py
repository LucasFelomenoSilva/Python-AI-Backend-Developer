def sacar(valor: float): # abertura do bloco método
    saldo = 500
    
    if saldo >= valor: # abertura do bloco if
        print("valor sacado")
        print("retire o seu dinheiro na boca do caixa.")
        
    print("Obrigado por ser nosso cliente, tenha um bom dia!")
    # fim do if    
# fim do método        

def depositar(valor):
    saldo = 500
    saldo += valor
    

sacar(500)