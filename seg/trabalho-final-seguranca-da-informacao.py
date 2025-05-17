# Alunos: André Heller, Luigi Garcia Marchetti e Martin Lange de Assis
# Professor: Gilvan Justino
# Instituição: FURB

from IPython.display import display, clear_output
import pandas as pd
import numpy as np
import io
import cv2
import matplotlib.pyplot as plt
from chave import *
from abrir_salvar_Arquivo import *


operacao = int(input('Selecione a operação desejada: \n 0 - Cifrar \n 1 - Decifrar \n'))
print('Operação escolhida: ' + str(operacao))

if operacao == 0:
    print('Cifrar')
else:
    print('Decifrar')

# Processar a chave
chave = str(input('\n🔑 Informe a chave (exemplo: A,B,C,D,...): \n'))

#### Gerar a chave

gerar_round_keys(chave)

############ Geração do arquivo de Entrada ############

# Execução principal
caminho = selecionar_arquivo()
print(f"Arquivo selecionado: {caminho}")

if caminho:
    print(f"Arquivo selecionado: {caminho}")
    bits = arquivo_para_bits(caminho)
    print(f"{len(bits)} bits lidos do arquivo.")

matriz_Arquivo = mostrar_bytes_em_hex(bits)

print(matriz_Arquivo)

matriz_Arquivo = PKCS7_Padding(matriz_Arquivo)

print(matriz_Arquivo)


##### parte cifrar 

#matriz_Arquivo = matriz_Arquivo
#matriz_chave = chave_para_hex(chave)
    





