print('testando')

massa_arroz = 0.025

def quantidade(n):
    return 2**n

def peso_gramas(quantidade):
    peso_total = massa_arroz*quantidade/(150*10**6)
    return peso_total

for n in range(0, 64):
    print(n, "\t", quantidade(n), peso_gramas(quantidade(n)))