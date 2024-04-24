conta_normal = False
conta_universitaia = True

saldo = 2000
saque = 2450
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com sucesso, com o uso do cheque especial!")
    else:
        print("Saque não realizado por falta de saldo!")
elif conta_universitaia:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saque não realizado por falta de saldo")