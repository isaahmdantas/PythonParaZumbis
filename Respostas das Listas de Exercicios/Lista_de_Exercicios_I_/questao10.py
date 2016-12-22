# -*- coding: utf-8 -*-
# Curso: Python para Zumbis
# Professor: Fernando Masonori
# Autor(a): Isadora Dantas
# Data: 18 de Dezembro de 2016


# Questão 10: Escreva um programa para calcular a redução do tempo
# de vida de um fumante. Pergunte a quantidade de cigarros fumados
# por dia e quantos anos ele já fumou. Considere que um fumante perde
# 10 minutos de vida a cada cigarro, calcule quantos dias de vida um
# fumante perderá. Exiba o total de dias.

# Entrada de dados:
qtd_cigarros = int(input('Informe a quantidade de cigarros fumados por dia: '))
anos = int(input('Informe a quantos anos já fumou: '))


# Saida de dados:
cigarros_fumados = ((anos * 365) * qtd_cigarros)
dias_perdidos = ((cigarros_fumados * 10) / 24 )

print('Quantidade de cigarrados já fumados: ', cigarros_fumados)
print('Quantidade de dias perdidos de vida: ', dias_perdidos)
