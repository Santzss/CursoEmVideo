"""frase = 'Curso em Video Python'

print('analise:')
print(len(frase))
print(frase.count('o',0,13)) # conta quantas vezes uma letra apareceu em um texto
print(frase.find('Android')) # retorna '-1' (significa que nao foi encontrado)
print('Curso' in frase) # procura frase em textos
print(frase.replace('Python','Android')) # Troca uma frase por outra / para receber o valor escreve 'frase ='
print(frase.upper()) # fica tudo em maiusculo
print(frase.lower()) # fica tudo em minusculo
print(frase.capitalize()) # deixa apenas o primeiro caractere em maiusculo
print(frase.title()) # deixara todos os caracteres em maiusculo(apenas a inicial)
print('=' * 20)
# ==================================================================================
print('trasformação:')
frase2 = "Aprendendo Python"
print(frase2.strip()) #remove todos os espaços inutes
print(frase2.rstrip()) #remove somente espaços inutes da direita
print(frase2.lstrip()) # remove somente os espaços inutes da esquerda
print('=' * 20)
# =======================================================================================
print("Divisão: ")
print(frase.split()) #vai dividir uma string em uma lista, onde cada elemento vai ser separado pelo seu splitador
print('-'.join(frase)) #vai juntar as string usando o '-'
print("=" * 20)
#===================================================================================
print('''......................................
...........................................................
..........................................
................''') #usa ''' para escrever textos longos na tela
"""

'''
print("EX022: ")
nome = str(input("Digite seu nome completo: "))
print("Em maiusculo:",nome.upper())
print("Em minusculo:",nome.lower())
print("Letras ao todo:",len(nome.replace(" ","")))
dividido = nome.split()
print("Primeiro nome:", len(dividido[0]))
print("=" * 30)
'''
'''
print("EX023: ")
numero = str(input("Digite um numero de 0 a 9999: "))
print("Unidade:",numero[3])
print("Dezena:", numero[2])
print("Centena:",numero[1])
print("Milhar:",numero[0])
'''

'''
print("EX024: ")
cidade = str(input("Digite o nome da sua cidade: "))
maiusculo2 = cidade.upper()
if "SANTO" in cidade:
    print("Sua cidade tem 'SANTO' no nome")
else:
    print("Sua cidade não tem 'SANTO' no nome")
'''

'''
print("Ex025: ")
nome2 = str(input("Digite seu nome: "))
maiusculo = nome2.upper()
if "SILVA" in maiusculo:
    print("Voce tem silva no nome")
else:
    print("voce nao tem silva no nome")
'''

print("EX026:")
frase = str(input("Digite uma frase:")).lower()
fa = frase.find('a')
fl = frase.rfind('a')

print("A letra 'a', apareceu:",frase.count('a'))
print("A letra 'a' aparece pela primeira vez na posição:",fa)
print("A letra 'a' aparece pela ultima vez na posição:",fl)

