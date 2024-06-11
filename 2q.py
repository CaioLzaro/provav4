#Faça uma função que informe a quantidade de dígitos de um determinado número informado
entrada = int(input("Digite um número:"))

def quantidade(entrada):
    entrada_str = str(entrada)
    return len(entrada_str)

print("O número possui", quantidade(entrada), "Dígitos.")