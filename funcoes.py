from random import random

def joga_moeda():
    valor = random()
    if valor> 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())


'Aln'