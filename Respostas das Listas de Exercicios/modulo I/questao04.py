# -*- coding: utf-8 -*-
# Curso: Python para Zumbis
# Professor: Fernando Masonori
# Autor(a): Isadora Dantas
# Data: 18 de Dezembro de 2016


# Questão 04: Faça um programa que calcule o aumento de um salário
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

# Entrada de dados:
salario = float(input('Informe o valor do seu salário: '))
porcentagem = float(input('Informe a porcentagem do aumento do salário: '))

novo_salario = (salario + (salario * (porcentagem / 100)))
aumento = novo_salario - salario

# Saida de dados:
print ('O aumento do salário foi de R$ %.2f' %aumento)
print ('Seu novo salário será de R$ %.2f' %novo_salario)

