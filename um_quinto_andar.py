#Calculo de Alguem de Imoveis

print('1/5 Andar')

val_imovel = float(input('Insira o valor do Imovel : '))
tipo_imovel = int(input('Informe o tipo do Imóvel:\n Digite [1] Casa ou [2] Apartamento : '))

if tipo_imovel == 2:
    valor_condominio = float(input('Informe o valor do Conodminio. Digite 0 caso nao possua : '))
    if valor_condominio == 0:
        None
    else:
        print(valor_condominio)
elif tipo_imovel == 1:
    alugel = val_imovel*0.55
    print(alugel)