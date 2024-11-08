from datetime import date

atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print(f"Quem nasceu em {nascimento} tem {idade} em {atual}")
if idade == 18:
    print("Voce tem que se alistar imediatamente")
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f"Voce ainda nao tem 18 anos. Ainda faltam {saldo} para o alistamento")
    print(f"Ainda faltam {ano} para voce se alistar")
else:
    saldo2 = idade - 18
    ano2 = atual - saldo2
    print(f"Voce ja deveria ter se alistado a {saldo2} anos")
    print(f"seu alistamento foi em {ano2}")