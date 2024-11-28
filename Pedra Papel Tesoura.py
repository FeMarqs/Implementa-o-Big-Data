# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tz6nAn0k_NP_sCniAF29Ih_FFKncNRSR
"""



"""Lista de Exercícios 3

3- faça um jogo de Pedra, Papel e Tesoura. No qual você digitará a letra P para jogar Papel, a letra R para jogar Pedra e a letra T para jogar Tesoura. Você jogará contra o computador e contabilizar o número de vitórias, empates e derrotas. ✌ ✋ ✊
"""

import random

def jogo_pedra_papel_tesoura():
    vitorias = 0
    empates = 0
    derrotas = 0

    while True:
        # Solicita a escolha do usuário
        print("\nEscolha uma opção:")
        print("P - Pedra")
        print("P - Papel")
        print("T - Tesoura")
        escolha_usuario = input("Digite P, R ou T (ou 'sair' para encerrar): ").upper()

        if escolha_usuario == 'SAIR':
            break
        elif escolha_usuario not in ['P', 'R', 'T']:
            print("Escolha inválida! Tente novamente.")
            continue

        # Gera a escolha do computador
        escolha_computador = random.choice(['P', 'R', 'T'])
        print(f"Computador escolheu: {escolha_computador}")

        # Verifica o resultado
        if escolha_usuario == escolha_computador:
            print("Empate!")
            empates += 1
        elif (escolha_usuario == 'P' and escolha_computador == 'R') or \
             (escolha_usuario == 'R' and escolha_computador == 'T') or \
             (escolha_usuario == 'T' and escolha_computador == 'P'):
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu!")
            derrotas += 1

        # Exibe o placar atual
        print(f"\nPlacar atual: Vitórias: {vitorias} | Empates: {empates} | Derrotas: {derrotas}")

# Chama a função principal para rodar o jogo
jogo_pedra_papel_tesoura()