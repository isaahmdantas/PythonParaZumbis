# -*- coding: utf-8 -*-
# Curso: Python para Zumbis
# Professor: Fernando Masonori
# Autor(a): Isadora Dantas
# Data: 18 de Dezembro de 2016


# Questão 09: Escreva um programa que pergunte a quantidade de
# km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia
# e R$ 0,15 por km rodado:

# Entrada de dados:
km = int(input('Informe a quantidade de km que será percorridos pelo carro: '))
dias = int(input('Informe o numero de dias que o carro foi alugado: '))



# Saida de dados:
pagamento = ((km * 0.15) + (dias * 60))

print ('O valor do aluguel será de R$ %.2f' %pagamento)
