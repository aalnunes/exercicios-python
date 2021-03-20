# faça um programa que peça dois numeros e impra o maior dele


lista = []
num = 1
while num in range(1,2):
    numeroadd = float(input('Insira um numero :'))
    resultado = lista.append(numeroadd)
    tamanho_da_lista = len(lista)
    num = tamanho_da_lista
    
print(max(lista))



