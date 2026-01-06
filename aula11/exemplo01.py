# Bibliotecas
import random


# random.randint --> numeros inteiros aleatórios

# n = random.randint(1, 10)
# m = random.randint(1, 10)
# print(n, m)

# ----------------------------------------------

# Gerar numeros decimais
# (o ':.2f' serve para limitar as casas decimais até 2)
# o 'round' serve para arredondar os numeros

n_decimal = random.uniform(1, 10)
print(f'{n_decimal:.2f}')
numero_decimal = round(n_decimal, 1)
print(numero_decimal)