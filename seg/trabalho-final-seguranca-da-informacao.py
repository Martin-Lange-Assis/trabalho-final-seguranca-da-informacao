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
from cifrar import *


# Processar a chave
# chave = str(input('\n🔑 Informe a chave (exemplo: A,B,C,D,...): \n'))
chave = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P'

#### Gerar a chave

matriz_chave = gerar_round_keys(chave)
# print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" + str(len(a)))
############ Geração do arquivo de Entrada ############

# Execução principal
caminho = selecionar_arquivo()
print(f"Arquivo selecionado: {caminho}")

if caminho:
    print(f"Arquivo selecionado: {caminho}")
    bits = arquivo_para_bits(caminho)
    print(f"{len(bits)} bits lidos do arquivo.")

matriz_Arquivo = mostrar_bytes_em_hex(bits)
matriz_Arquivo_padding = PKCS7_Padding(matriz_Arquivo)
print(f"\n🔒 matriz_Arquivo_padding {matriz_Arquivo_padding} ")

# operacao = int(input('Selecione a operação desejada: \n 0 - Cifrar \n 1 - Decifrar \n'))
operacao = 0
print('Operação escolhida: ' + str(operacao))

if operacao == 0:
    print('Cifrar')
    #blocos_cifrados = cifrar_aes(matriz_Arquivo_padding, matriz_chave)
else:
    print('Decifrar')

##### parte cifrar 

#matriz_Arquivo = matriz_Arquivo
# matriz_chave = chave_para_hex(chave_round_key)

# add_round_key(matriz_Arquivo_padding, matriz_chave[0])


# Divide a matriz_Arquivo em blocos de 4x4
# Junta cada dois blocos de 2 linhas em um bloco de 4 linhas

blocos_arquivo = agrupar_blocos_arquivo(matriz_Arquivo_padding)
print(f"\n🔒 agrupar_blocos_arquivo {blocos_arquivo} ")

blocos_chave = agrupar_blocos_chave(matriz_chave)
print(f"\n🔒 agrupar_blocos_chave {blocos_chave} ")
# Aplica a operação em cada bloco com a mesma chave
# resultados = [add_round_key(bloco, matriz_chave) for bloco in blocos_arquivo]


aplicar_add_round_key_blocos_etapa01 = aplicar_add_round_key_blocos(blocos_arquivo, blocos_chave)

substituidas_SBox_Etapa2 = substituir_Sbox_Etapa02(aplicar_add_round_key_blocos_etapa01)

matriz_shift_rows_Etapa03 = shift_rows_blocos(substituidas_SBox_Etapa2)

resultado_mix_columns_Etapa04 = mix_columns(matriz_shift_rows_Etapa03)

resultado_addroundkey = add_round_key5(resultado_mix_columns_Etapa04, matriz_chave)

with open("./files/encrypted.bin", "wb") as f:
    f.write(resultado_addroundkey)


print("\n---------------------------------\n")



