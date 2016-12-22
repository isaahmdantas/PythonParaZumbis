# -*- coding: utf-8 -*-
# Curso: Python para Zumbis
# Professor: Fernando Masonori
# Autor(a): Isadora Dantas
# Data: 18 de Dezembro de 2016


# Questão 07: Converta uma temperatura digitada em Celsius
# para Fahrenheit. F = 9*C/5 + 32

# Entrada de dados:
celsius = int(input('Informe a temperatura em celsius: '))

# Saida de dados:
fahrenheit = ((9 * (celsius / 5)) + 32)

print('A temperatura em fahrenheit: %.1f' %fahrenheit, 'Fº')
