a, b, c = map(int, input("Digite 3 números inteiros:").split())

def maior(a, b, c):
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    else:
        return c
        
resultado = maior(a, b, c)
print("O maior número é:", resultado)   
