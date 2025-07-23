n1 = int(input("Adicione um número par para ser calculado com o número 2: "))
n2 = 2
resto = n1 % n2
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
while resto != 0:
    print("Você não adicionou um número par, tente novamente:")
    n1 = int(input("Adicione um número par para ser calculado com o número 2: "))
    resto = n1 % n2
print(f"A tabela entre os números {n1} e {n2} ficou da seguinte forma: ")
print(f"soma: {soma}")
print(f"subtração: {sub}")
print(f"multiplicação: {multi}")
print(f"divisão: {div}")
