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
from cifragem import *


# operacao = int(input('Selecione a operação desejada: \n 0 - Cifrar \n 1 - Decifrar \n'))
operacao = '0 - Cifrar'
print('Operação escolhida: ' + str(operacao))

if operacao == 0:
    print('Cifrar')
else:
    print('Decifrar')

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


# print(matriz_Arquivo)

# A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P
##### parte cifrar 

#matriz_Arquivo = matriz_Arquivo
# matriz_chave = chave_para_hex(chave_round_key)

# add_round_key(matriz_Arquivo_padding, matriz_chave[0])

def dividir_em_blocos_4x4(matriz):
    blocos = []
    num_blocos = len(matriz[0]) // 4  # 8 colunas -> 2 blocos

    for b in range(num_blocos):
        bloco = []
        for linha in matriz:
            bloco.append(linha[b*4:(b+1)*4])
        blocos.append(bloco)
    return blocos

def add_round_key(matriz_Arquivo, matriz_chave):
    resultado = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor_xor = int(matriz_Arquivo[i][j], 16) ^ int(matriz_chave[i][j], 16)
            linha.append(f"0x{valor_xor:02x}")
        resultado.append(linha)
    return list(zip(*resultado))




# Divide a matriz_Arquivo em blocos de 4x4
blocos_arquivo = dividir_em_blocos_4x4(matriz_Arquivo)

# Aplica a operação em cada bloco com a mesma chave
resultados = [add_round_key(bloco, matriz_chave) for bloco in blocos_arquivo]

# Exibe os resultados de cada bloco
# Lista para armazenar as palavras substituídas de todos os blocos
palavras_substituidas = []

# Exibe os resultados de cada bloco
# Lista para armazenar as palavras substituídas (em hexadecimal) de todos os blocos
palavras_substituidas = []

# Exibe os resultados de cada bloco
for idx, resultado in enumerate(resultados):
    print(f"\n🔒 Bloco {idx+1} cifrado:")
    for linha_idx, linha in enumerate(resultado):
        print(' '.join(linha))
        nova_linha = []
        for palavra_idx, palavra in enumerate(linha):
            palavra_int = int(palavra, 16) if isinstance(palavra, str) and palavra.startswith('0x') else palavra
            palavra_bytes = palavra_int.to_bytes(1, byteorder='big')
            nova_palavra = substituicao_palavra(palavra_bytes)
            nova_linha.append(f"0x{nova_palavra[0]:02x}")  # Armazena como string hexadecimal
            print(f"Palavra original: {palavra} -> Substituída: 0x{nova_palavra[0]:02X}")
        palavras_substituidas.append(nova_linha)

# Exemplo de uso: mostrar a lista final
print("\n📦 Lista final com palavras substituídas (hex):")
for linha in palavras_substituidas:
    print(' '.join(linha))


# Agora 'palavras_substituidas' é uma lista de listas, onde cada sublista é uma linha com os bytes substituídos




# chave_round_key_0 = add_round_key(matriz_Arquivo, matriz_chave)
