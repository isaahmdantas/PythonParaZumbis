# -*- coding: utf-8 -*-
# Curso: Python para Zumbis
# Professor: Fernando Masonori
# Autor(a): Isadora Dantas
# Data: 18 de Dezembro de 2016


# Questão 08: Converta uma temperatura digitada em  Fahrenheit para Celsius.

# Entrada de dados:
fahrenheit = int(input('Informe a temperatura em fahrenheit: '))

# Saida de dados:
celsius = (fahrenheit - 32) / 1.8

print('A temperatura em celsius: %.1f' %celsius, 'Cº')
