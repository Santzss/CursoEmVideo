import pygame

# caso a idade seja maior que 18, vai tocar uma musica
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if idade > 18:
    print(f"Seja bem vindo {nome}")
    pygame.init()
    pygame.mixer.music.load('tocandoMp3.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else:
    print("Voce ainda nao tem idade suficiente!")
