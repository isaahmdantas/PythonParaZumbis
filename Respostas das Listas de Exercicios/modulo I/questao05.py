# -*- coding: utf-8 -*-
# Curso: Python para Zumbis
# Professor: Fernando Masonori
# Autor(a): Isadora Dantas
# Data: 18 de Dezembro de 2016


# Questão 05: Solicite o preço de uma mercadoria e o percentual de desconto
# Exiba o valor do desconto e o preço pagar.

# Entrada de dados:
preco = float(input('Informe o preço da mercadoria: '))
percentual = float(input('Informe a percentual de desconto: '))

novo_preco = (preco - (preco * (percentual / 100)))
desconto = preco - novo_preco
# Saida de dados:
print ('O desconto da mercadoria foi de R$ %.2f' %desconto)
print ('O novo valor da mercadoria  será de R$ %.2f' %novo_preco)
