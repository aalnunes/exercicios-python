'''
Aula de Funções _ Geek University

Funçoes sao partes de codigos que realizam tarefas especificas
Podem ou nao receber entradas de dados e retornar uma saida de dados


Definindo uma função

def nome_da_função(Parametros de Entrada):
    bloco_da_função
    
Onde :

==> Nome da função sempre devera ser com letras minusculas, caso seja composto separado por underline (_)
ex:

def alisson_lima ():
    bloco_da_funçao
    
==> parametro de Entrada
Opcionais onde  tendo mais de um , cada um separado por virgulas podendo ser opcionais ou nao :

==> Bloco da funçao
    Tambem chamado de corpo ou implementação da funçao , e onde o processamento da funçao acontece.
    neste bloco pode ter ou nao retorno da funçao.
    

==> Observação:
    Veja que para definir uma função  ultilizamos a palavra  'def' informando ao  python que estamos definindo uma funçao.
    também abrimos o bloco de codigo com o ja conhecido dois pontos : que ja e conhecido em python para definir blocos.
  

'''

# Definindo minha primeira função

def diz_oi():
    print('Oi!')


# Nota_se que ao utilizar a função devemos chamar o nome da função finalizado com os ()
    
diz_oi()

#Exemplo II

def cantar_parabens():
    print('Parabéns pra você')
    print('nesta Data querida')
    print('Muitas Felicidades')
    print('Muitos Anos de vida')
    print('Vivaaa COmunista!!!')
    
#Chamando a Função

#cantar_parabens()

#Utilizando a funçao com um agregado
"""
for n in range(1,5):
    cantar_parabens()"""
    
    
'''def dizer():
    return 'Ola Mundo'

dizer()
print(dizer())'''


# Definindo uma função mais complexa

''''jogar Cara ou Coroa'

from funcoes import joga_moeda

joga_moeda()'''


#   Aqui testerai algumas possibilidades com funções


print('Insira seu nome abaixo e veja o que acontece :')

nome = input('Insira seu nome :')
sobrenome = input('Insira seu sobre nome :')

def mostrar_nome (a= nome,b=sobrenome):
    print(f' Ola senhor {nome} {sobrenome}')

mostrar_nome()
