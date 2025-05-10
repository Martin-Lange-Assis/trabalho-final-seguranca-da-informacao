# Alunos: André Heller, Luigi Garcia Marchetti e Martin Lange de Assis
# Professor: Gilvan Justino
# Instituição: FURB

from IPython.display import display, clear_output
import pandas as pd
import numpy as np
import io
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
import geracao
from tkinter import filedialog

operacao = int(input('Selecione a operação desejada: \n 0 - Cifrar \n 1 - Decifrar \n'))
print('Operação escolhida: ' + str(operacao))

if operacao == 0:
    print('Cifrar')
else:
    print('Decifrar')

chave = str(input('\n🔑 Informe a chave: \n'))

chave = geracao.gerar_chave(chave)



def selecionar_arquivo():
    """Abre uma janela para o usuário selecionar um arquivo para leitura."""
    root = tk.Tk()
    root.withdraw()
    caminho = filedialog.askopenfilename(title="Selecione um arquivo para ler")
    return caminho

def selecionar_destino():
    """Abre uma janela para o usuário escolher onde salvar o novo arquivo."""
    root = tk.Tk()
    root.withdraw()
    caminho = filedialog.asksaveasfilename(
        title="Selecione onde salvar o arquivo", defaultextension=".bin"
    )
    return caminho

def arquivo_para_bits(caminho_arquivo):
    """Converte o conteúdo de um arquivo em uma lista de bits."""
    with open(caminho_arquivo, 'rb') as f:
        dados = f.read()
        lista_bits = []
        for byte in dados:
            bits = format(byte, '08b')
            lista_bits.extend(bits)
        return lista_bits

def bits_para_arquivo(lista_bits, caminho_saida):
    """Reconstrói um arquivo a partir de uma lista de bits."""
    if len(lista_bits) % 8 != 0:
        print(f"Aviso: número de bits ({len(lista_bits)}) não é múltiplo de 8. Truncando para reconstrução.")
        lista_bits = lista_bits[:len(lista_bits) - (len(lista_bits) % 8)]

    bytes_data = bytearray()
    for i in range(0, len(lista_bits), 8):
        byte_str = ''.join(lista_bits[i:i+8])
        byte = int(byte_str, 2)
        bytes_data.append(byte)

    with open(caminho_saida, 'wb') as f:
        f.write(bytes_data)

# Execução principal
caminho = selecionar_arquivo()
if caminho:
    print(f"Arquivo selecionado: {caminho}")
    bits = arquivo_para_bits(caminho)
    print(f"{len(bits)} bits lidos do arquivo.")
    print(f" bits: ({bits}).")

    caminho_saida = selecionar_destino()
    if caminho_saida:
        bits_para_arquivo(bits, caminho_saida)
        print(f"Arquivo reconstruído com sucesso em: {caminho_saida}")
    else:
        print("Nenhum local de salvamento foi escolhido.")
else:
    print("Nenhum arquivo foi selecionado.")

def pegar_bytes(upload_widget):
    if upload_widget.value:
        nome_arquivo = list(upload_widget.value.keys())[0]
        dados_arquivo = upload_widget.value[nome_arquivo]['content']
        return dados_arquivo  # isso são os bytes
    else:
        print("Nenhum arquivo enviado ainda.")
        return None

#bytesDoArquivo = pegar_bytes(upload)

