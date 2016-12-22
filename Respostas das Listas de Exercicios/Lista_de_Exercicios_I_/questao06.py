# -*- coding: utf-8 -*-
# Curso: Python para Zumbis
# Professor: Fernando Masonori
# Autor(a): Isadora Dantas
# Data: 18 de Dezembro de 2016


# Questão 06: Calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média
# esperada para a viagem.

# Entrada de dados:
distancia = float(input('Informe a distancia que deseja pecorrer: '))
velocidade_media = float(input('Informe a velocidade média esperada para viagem: '))

# Saida de dados:
tempo = distancia / velocidade_media
print("Tempo pecorrido na viagem:  %.1f" %tempo, 's')
