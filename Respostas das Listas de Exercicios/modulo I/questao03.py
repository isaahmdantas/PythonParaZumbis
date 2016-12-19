# -*- coding: utf-8 -*-
# Curso: Python para Zumbis
# Professor: Fernando Masonori
# Autor(a): Isadora Dantas
# Data: 18 de Dezembro de 2016


# Questão 03: Escreva um programa que leia a quantidade de dias
# horas, minutos e segundos do usuário. Calcule o total em segundos.

# Entrada de dados:
dias = int(input('Informe o número de dias: '))
horas = int(input('Informe o número de horas: '))
minutos = int(input('Informe o número de minutos: '))
segundos = int(input('Informe o número de segundos: '))

# Saida de dados:
horas = horas + dias * 24
minutos = minutos + horas * 60
total_segundos = (segundos + (minutos * 60))

print ("Total em segundos: ", total_segundos, 'segundo(s)') 
