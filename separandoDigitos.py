entrada = int(input("Informe um número: "))
u = entrada // 1 % 10
d = entrada // 10 % 10
c = entrada // 100 % 10
m = entrada // 1000 % 10
print(f"Analisando o numero: {entrada}")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")

