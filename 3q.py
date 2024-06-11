a = int(input("Digite a base: "))
b = int(input("Digite a potência: "))
c = 1

if b >= 0:
    for i in range(b):
        c *= a
else:
    for i in range(-b):
        c /= a

print("Resultado:", c)

    

    
    