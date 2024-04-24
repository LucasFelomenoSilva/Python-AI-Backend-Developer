curso = "Curso de Python"
nome_curso = curso
saldo, limite = 1000, 500

curso is nome_curso

curso is not nome_curso

print(saldo is limite)
# não ocupam a mesma região de memoria
print(saldo is not limite)
# indicando que ocupam a mesma região