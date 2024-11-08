valorCasa = float(input("Qual o valor da casa? "))
salario = float(input("Digite o seu salario: "))
anos = int(input("Em quantos anos pretende pagar o imovel? "))

calc = valorCasa / anos

if salario / calc > 30:
    print("Voce não podera comprar o imovel! ")
else:
    print("Imovel comprado com sucesso!")