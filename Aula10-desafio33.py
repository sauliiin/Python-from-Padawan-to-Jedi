# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite um número inteiro:'))
b = int(input('Digite um outro inteiro diferente:'))
c = int(input('Digite só mais um número inteiro:'))
if a > b and a > c:
    maior = a
if b > c and b > a:
    maior = b
if c > a and c > a:
    maior = c
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
if a < b and a > c:
    medio = a
if b < c and b > a:
    medio = b
if c < a and c > b:
    medio = c
print('A ordem crescente dos valores é: {}, {} e {}.'.format(menor, medio, maior))

