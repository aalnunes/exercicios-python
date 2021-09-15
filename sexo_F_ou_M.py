# Ao o informar a letra F devera retornar Feminino e M para Masculino, caso contratrario sexo invalido

sexo = input('Informe : \n [F] para Feminino \n [M] para Masculino \n ___:')

if sexo == 'F':
    print('Sexo Feminino')
elif sexo == 'M':
    print('Sexo Masculino')
else:
    print('Sexo indefinido...Decide')
