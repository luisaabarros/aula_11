import os
import random


def numeros(i, f, q):
    lst_n = [random.randint(i, f) for n in range(q)]
    return lst_n


def soma(x, y):
    s = (x + y)
    return s


def subtraçao(x, y):
    su = (x - y)
    return su


def multiplicaçao(x, y):
    m = (x * y)
    return m


def divisao(x, y):
    d = (x / y)
    return d


inicio = int(input('Forneça o número inicial: '))
final = int(input('Forneça o número final: '))
quantidade = 2
lst_numeros = numeros(inicio, final, quantidade)

print(lst_numeros)

x = (lst_numeros[0])
y = (lst_numeros[1])

som = soma(x, y)

sub = subtraçao(x, y)

multi = multiplicaçao(x, y)

divi = divisao(x, y)

print(f'Soma: {som}\nSubtração: {sub}\nMultiplicação: {multi}\nDivisão: {divi}')