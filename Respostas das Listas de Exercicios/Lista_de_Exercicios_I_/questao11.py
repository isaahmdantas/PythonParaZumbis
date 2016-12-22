# -*- coding: utf-8 -*-
# Curso: Python para Zumbis
# Professor: Fernando Masonori
# Autor(a): Isadora Dantas
# Data: 18 de Dezembro de 2016


# Questão 11: Sabendo que str( ) converte valores numéricos para string,
# calcule quantos dígitos há em 2 elevado a um milhão.

# Entrada de dados:


# Saida de dados:
potencia = 2**1000000
potencia_string = str(potencia)
tamanho_potencia = len(potencia_string)

print ('A quantidade de digitos ha em 2 ^^ 1000000 é: ', tamanho_potencia)
