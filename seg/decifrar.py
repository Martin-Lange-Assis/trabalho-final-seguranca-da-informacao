# decifrar.py
from cifrar import galois_mult, aplicar_add_round_key_blocos
from chave import sbox

# Inverso da S-Box
inv_sbox = [0] * 256
for i in range(16):
    for j in range(16):
        val = sbox[i][j]
        inv_sbox[val] = (i << 4) | j

def inv_add_round_key5_blocos(bloco_estado, bloco_chave):
    return aplicar_add_round_key_blocosDecifragem(bloco_estado, bloco_chave)

def aplicar_add_round_key_blocosDecifragem(bloco_estado, bloco_chave):
    resultado = []
    for linha_estado, linha_chave in zip(bloco_estado, bloco_chave):
        nova_linha = []
        for val_estado, val_chave in zip(linha_estado, linha_chave):
            xor_result = int(val_estado, 16) ^ int(val_chave, 16)
            nova_linha.append(f"0x{xor_result:02x}")
        resultado.append(nova_linha)
    return resultado

def inv_mix_columns_blocos(matriz):
    blocos = [matriz[i:i+4] for i in range(0, len(matriz), 4)]
    blocos_mix = []

    inv_mult_matrix = [
        [14, 11, 13, 9],
        [9, 14, 11, 13],
        [13, 9, 14, 11],
        [11, 13, 9, 14]
    ]

    for bloco in blocos:
        for i in range(4):
            for j in range(4):
                if isinstance(bloco[i][j], str):
                    bloco[i][j] = int(bloco[i][j], 16)
        result = [[0] * 4 for _ in range(4)]

        for col in range(4):
            coluna = [bloco[linha][col] for linha in range(4)]
            for linha in range(4):
                valor = 0
                for k in range(4):
                    a = coluna[k]
                    b = inv_mult_matrix[linha][k]
                    mult = galois_mult(a, b) if b != 1 else a
                    valor ^= mult
                result[linha][col] = valor

        blocos_mix.extend(result)
    return blocos_mix

def inv_shift_rows_blocos(linhas_blocos):
    blocos = [linhas_blocos[i:i+4] for i in range(0, len(linhas_blocos), 4)]
    blocos_shifted = []

    for bloco in blocos:
        novo_bloco = []
        for i in range(4):
            nova_linha = bloco[i][-i:] + bloco[i][:-i]
            novo_bloco.append(nova_linha)
        blocos_shifted.extend(novo_bloco)
    return blocos_shifted

def inv_substituir_Sbox_Etapa02(blocos):
    resultado = []
    for linha in blocos:
        nova_linha = []
        for byte in linha:
            if isinstance(byte, str):
                byte = int(byte, 16)
            inv_byte = inv_sbox[byte]
            nova_linha.append(f"0x{inv_byte:02x}")
        resultado.append(nova_linha)
    return resultado

def inv_add_round_key1_blocos(bloco_estado, blocos_chave):
    return aplicar_add_round_keyfinal_blocos(bloco_estado, blocos_chave)

def aplicar_add_round_keyfinal_blocos(bloco_estado, blocos_chave):
    resultado = []
    num_blocos = min(len(blocos_chave), len(bloco_estado) // 4)
    for bloco_idx in range(num_blocos):
        for linha_idx in range(4):
            index = bloco_idx * 4 + linha_idx
            linha_estado = bloco_estado[index]
            linha_chave = blocos_chave[bloco_idx][linha_idx]
            linha_resultante = []
            for byte_estado, byte_chave in zip(linha_estado, linha_chave):
                xor_byte = int(byte_estado, 16) ^ int(byte_chave, 16)
                linha_resultante.append(f"0x{xor_byte:02X}")
            resultado.append(linha_resultante)
    return resultado



def dividir_em_blocos_4x4(matriz):
    blocos = [matriz[i:i+4] for i in range(0, len(matriz), 4)]
    return blocos


def linearizar_blocos(blocos_4x4):
    # Supondo blocos_4x4 é lista de blocos 4x4 (listas 4x4)
    linear = []
    for bloco in blocos_4x4:
        for linha in bloco:
            for byte in linha:
                linear.append(byte)
    return linear

def remover_PKCS7_padding(hex_lista):
    if not hex_lista:
        return hex_lista
    ultimo_valor = int(hex_lista[-1], 16)
    if all(int(b, 16) == ultimo_valor for b in hex_lista[-ultimo_valor:]):
        return hex_lista[:-ultimo_valor]
    return hex_lista
