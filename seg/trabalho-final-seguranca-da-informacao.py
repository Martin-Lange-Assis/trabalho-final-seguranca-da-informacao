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

print(f"\n🔒 matriz_Arquivo_padding {matriz_Arquivo_padding} ")


# A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P
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




# TESTANDO MIX_COLUMNS

def mix_columns(matriz_shift_rows_Etapa03):
    # Garante que todos os valores são inteiros (corrige possíveis strings hex)
    for i in range(4):
        for j in range(4):
            if isinstance(matriz_shift_rows_Etapa03[i][j], str):
                matriz_shift_rows_Etapa03[i][j] = int(matriz_shift_rows_Etapa03[i][j], 16)
    result = [[0] * 4 for _ in range(4)]
    mult_matrix = [
        [2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]
    ]

    for col in range(4):
        coluna = [matriz_shift_rows_Etapa03[linha][col] for linha in range(4)]
        for linha in range(4):
            valor = 0
            for k in range(4):
                a = coluna[k]
                b = mult_matrix[linha][k]
                if b == 1:
                    mult = a
                elif b == 2:
                    mult = galois_mult(a, 2)
                elif b == 3:
                    mult = galois_mult(a, 3)
                else:
                    raise ValueError("Valor inválido na matriz de multiplicação")
                valor ^= mult
            result[linha][col] = valor
    return result

resultado_mix_columns_Etapa04 = mix_columns(matriz_shift_rows_Etapa03)



# Exibir resultado em hex
# — ShiftRows já impresso acima —

# print()                          # 1 linha em branco
# # print("\n"*2)                  # se quiser 2 linhas em branco
# print("🔀 Resultado após MixColumns:\n")
# for linha in resultado_mix_columns_Etapa04:
#     print(' '.join(f'0x{int(byte, 16):02X}' for byte in linha))


def add_round_key5(mix_columns_state, resultados):
    print(resultados)
    resultado = []
    for i in range(4):
        linha = []
        for j in range(4):
            # mix_columns_state e round_key podem conter strings "0xXX" ou ints
            a = mix_columns_state[i][j]
            
            b = resultados[i][j]

            val_a = a if isinstance(a, int) else int(a, 16)
            val_b = b if isinstance(b, int) else int(b, 16)
            print(f"DEBUG - b na posição [{i}][{j}]: {b} (tipo {type(b)})")

            valor_xor = val_a ^ val_b
            linha.append(valor_xor)
        resultado.append(linha)
    return resultado


resultado_addroundkey = add_round_key5(resultado_mix_columns, matriz_chave)

# Imprime o resultado formatado em hex
for linha in resultado_addroundkey:
    print(' '.join(f"0x{byte:02X}" for byte in linha))





# print(' '.join(f'0x{byte:02X}' for byte in linha))

# Suponha que voce já tenha resultado_mixcolumns e round_key_rodada como 4x4
resultado_addroundkey = add_round_key5(resultado_mix_columns, resultado_addroundkey)

print("\n🔐 Resultado após AddRoundKey:\n")
for linha in resultado_addroundkey:
    print(' '.join(f'0x{byte:02X}' for byte in linha))
print("\n---------------------------------\n")



