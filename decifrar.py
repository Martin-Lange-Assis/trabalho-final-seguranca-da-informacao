from chave import *

def inv_shift_rows(matriz):
    """
    Aplica a operação InvShiftRows à matriz (4x4).
    Desloca as linhas para a direita conforme a posição da linha.
    """
    nova_matriz = []
    for i in range(4):
        linha = matriz[i]
        nova_linha = linha[-i:] + linha[:-i]
        nova_matriz.append(nova_linha)
    return nova_matriz
