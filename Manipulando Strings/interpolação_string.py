nome = "Lucas"
idade = 20
profissao = "Programador"
linguagem = "Python"
pontos = 45.4045445

dados = {"nome": "Lucas", "idade": 20, "profissao": "Programador", "linguagem": "Python", "pontos": 45.454}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome)) 
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(name=nome, age=idade))  
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Olá ! Me chamo {nome} e tenho {idade}!")

print("Olá ! Meu nome é nome {nome}, tenho {idade} e sonho em ser {profissao}.\nA linguagem que estudo hoje é {linguagem} e possuo {pontos} na plataforma Dio.".format(**dados))

print(f"Olá ! Me chamo {nome} e tenho {idade}! Possuo {pontos:.2f} na Dio.")