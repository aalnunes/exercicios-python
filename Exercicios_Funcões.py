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