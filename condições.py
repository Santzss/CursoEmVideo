'''
import random
N = int(input("Digite um numero inteiro entre 1 e 5: "))
aleatorio = random.randint(1,5)
if N == aleatorio:
    print("Voce venceu! ")
else:
    print("Voce perdeu!")
'''

'''
vel = int(input("Digite a velocidade do carro: "))

if vel > 80:
    multa = (vel - 80) * 7
    print(f"Voce estava acima do limite de velocidade, sua multa é de {multa} reais")
else:
    print("Voce esta dentro do padrao de velocidade!")
'''

'''
n = int(input("Digite um numero: "))
if n % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")
'''

'''
dis = int(input("Qual a distancia da viagem: "))
if dis <= 200:
    calc = dis * 0.50
    print(f"Sua viagem vai custar R${calc} por km rodados")
else:
    calc2 = dis * 0.45
    print(f"Sua viagem vai custar R${calc2} por km rodados")
'''

ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print("O ano é bissexto")
else:
    print("O ano nao é bisssexto")