#Calculo de Alguem de Imoveis
import locale

print('1/5 Andar')

val_imovel = float(input('Insira o valor do Imovel : '))
tipo_imovel = int(input('Informe o tipo do Imóvel:\n Digite [1] Casa ou [2] Apartamento : '))
quartos_imovel = int(input('Informe a quantidade de quartos do Imovel: '))


def currency (val):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    val = locale.currency(val, grouping=True)
    return val

    
if tipo_imovel == 1 and quartos_imovel ==1:
        aluguel_minimo = val_imovel*0.0044
        aluguel_maximo = val_imovel *0.0055
        print('O valor do alguel esta entre ' + currency(aluguel_minimo)+' e '+ currency(aluguel_maximo))
    
if tipo_imovel == 1 and quartos_imovel ==2:
        aluguel_minimo = val_imovel*0.0047
        aluguel_maximo = val_imovel *0.0058
        print('O valor do alguel esta entre ' + currency(aluguel_minimo)+' e '+ currency(aluguel_maximo))
    
if tipo_imovel == 1 and quartos_imovel ==3:
        aluguel_minimo = val_imovel*0.00529
        aluguel_maximo = val_imovel *0.00639
        print('O valor do alguel esta entre ' + currency(aluguel_minimo)+' e '+ currency(aluguel_maximo))
        
elif tipo_imovel == 2 and quartos_imovel ==1:
        condominio= float(input('Informe o valor do condominio: '))
        aluguel_minimo = val_imovel*0.00529 + condominio
        aluguel_maximo = val_imovel *0.00639 + condominio
        print('O valor do alguel esta entre ' + (currency(aluguel_minimo)) + ' e '+ currency(aluguel_maximo))
        
elif tipo_imovel == 2 and quartos_imovel ==2:
        condominio= float(input('Informe o valor do condominio: '))
        aluguel_minimo = val_imovel*0.00599 + condominio
        aluguel_maximo = val_imovel *0.00699 + condominio
        print('O valor do alguel esta entre ' + (currency(aluguel_minimo)) + ' e '+ currency(aluguel_maximo))        