from chave import substituicao_palavra

# Tabela E
E = [
    [0x01, 0x03, 0x05, 0x0F, 0x11, 0x33, 0x55, 0xFF, 0x1A, 0x2E, 0x72, 0x96, 0xA1, 0xF8, 0x13, 0x35],
    [0x5F, 0xE1, 0x38, 0x48, 0xD8, 0x73, 0x95, 0xA4, 0xF7, 0x02, 0x06, 0x0A, 0x1E, 0x22, 0x66, 0xAA],
    [0xE5, 0x34, 0x5C, 0xE4, 0x37, 0x59, 0xEB, 0x26, 0x6A, 0xBE, 0xD9, 0x70, 0x90, 0xAB, 0xE6, 0x31],
    [0x53, 0xF5, 0x04, 0x0C, 0x14, 0x3C, 0x44, 0xCC, 0x4F, 0xD1, 0x68, 0xB8, 0xD3, 0x6E, 0xB2, 0xCD],
    [0x4C, 0xD4, 0x67, 0xA9, 0xE0, 0x3B, 0x4D, 0xD7, 0x62, 0xA6, 0xF1, 0x08, 0x18, 0x28, 0x78, 0x88],
    [0x83, 0x9E, 0xB9, 0xD0, 0x6B, 0xBD, 0xDC, 0x7F, 0x81, 0x98, 0xB3, 0xCE, 0x49, 0xDB, 0x76, 0x9A],
    [0xB5, 0xC4, 0x57, 0xF9, 0x10, 0x30, 0x50, 0xF0, 0x0B, 0x1D, 0x27, 0x69, 0xBB, 0xD6, 0x61, 0xA3],
    [0xFE, 0x19, 0x2B, 0x7D, 0x87, 0x92, 0xAD, 0xEC, 0x2F, 0x71, 0x93, 0xAE, 0xE9, 0x20, 0x60, 0xA0],
    [0xFB, 0x16, 0x3A, 0x4E, 0xD2, 0x6D, 0xB7, 0xC2, 0x5D, 0xE7, 0x32, 0x56, 0xFA, 0x15, 0x3F, 0x41],
    [0xC3, 0x5E, 0xE2, 0x3D, 0x47, 0xC9, 0x40, 0xC0, 0x5B, 0xED, 0x2C, 0x74, 0x9C, 0xBF, 0xDA, 0x75],
    [0x9F, 0xBA, 0xD5, 0x64, 0xAC, 0xEF, 0x2A, 0x7E, 0x82, 0x9D, 0xBC, 0xDF, 0x7A, 0x8E, 0x89, 0x80],
    [0x9B, 0xB6, 0xC1, 0x58, 0xE8, 0x23, 0x65, 0xAF, 0xEA, 0x25, 0x6F, 0xB1, 0xC8, 0x43, 0xC5, 0x54],
    [0xFC, 0x1F, 0x21, 0x63, 0xA5, 0xF4, 0x07, 0x09, 0x1B, 0x2D, 0x77, 0x99, 0xB0, 0xCB, 0x46, 0xCA],
    [0x45, 0xCF, 0x4A, 0xDE, 0x79, 0x8B, 0x86, 0x91, 0xA8, 0xE3, 0x3E, 0x42, 0xC6, 0x51, 0xF3, 0x0E],
    [0x12, 0x36, 0x5A, 0xEE, 0x29, 0x7B, 0x8D, 0x8C, 0x8F, 0x8A, 0x85, 0x94, 0xA7, 0xF2, 0x0D, 0x17],
    [0x39, 0x4B, 0xDD, 0x7C, 0x84, 0x97, 0xA2, 0xFD, 0x1C, 0x24, 0x6C, 0xB4, 0xC7, 0x52, 0xF6, 0x01]
]

# Tabela L

L = [
    [0x00, 0x00, 0x19, 0x01, 0x32, 0x02, 0x1A, 0xC6, 0x4B, 0xC7, 0x1B, 0x68, 0x33, 0xEE, 0xDF, 0x03],
    [0x64, 0x04, 0xE0, 0x0E, 0x34, 0x8D, 0x81, 0xEF, 0x4C, 0x71, 0x08, 0xC8, 0xF8, 0x69, 0x1C, 0xC1],
    [0x7D, 0xC2, 0x1D, 0xB5, 0xF9, 0xB9, 0x27, 0x6A, 0x4D, 0xE4, 0xA6, 0x72, 0x9A, 0xC9, 0x09, 0x78],
    [0x65, 0x2F, 0x8A, 0x05, 0x21, 0x0F, 0xE1, 0x24, 0x12, 0xF0, 0x82, 0x45, 0x35, 0x93, 0xDA, 0x8E],
    [0x96, 0x8F, 0xDB, 0xBD, 0x36, 0xD0, 0xCE, 0x94, 0x13, 0x5C, 0xD2, 0xF1, 0x40, 0x46, 0x83, 0x38],
    [0x66, 0xDD, 0xFD, 0x30, 0xBF, 0x06, 0x8B, 0x62, 0xB3, 0x25, 0xE2, 0x98, 0x22, 0x88, 0x91, 0x10],
    [0x7E, 0x6E, 0x48, 0xC3, 0xA3, 0xB6, 0x1E, 0x42, 0x3A, 0x6B, 0x28, 0x54, 0xFA, 0x85, 0x3D, 0xBA],
    [0x2B, 0x79, 0x0A, 0x15, 0x9B, 0x9F, 0x5E, 0xCA, 0x4E, 0xD4, 0xAC, 0xE5, 0xF3, 0x73, 0xA7, 0x57],
    [0xAF, 0x58, 0xA8, 0x50, 0xF4, 0xEA, 0xD6, 0x74, 0x4F, 0xAE, 0xE9, 0xD5, 0xE7, 0xE6, 0xAD, 0xE8],
    [0x2C, 0xD7, 0x75, 0x7A, 0xEB, 0x16, 0x0B, 0xF5, 0x59, 0xCB, 0x5F, 0xB0, 0x9C, 0xA9, 0x51, 0xA0],
    [0x7F, 0x0C, 0xF6, 0x6F, 0x17, 0xC4, 0x49, 0xEC, 0xD8, 0x43, 0x1F, 0x2D, 0xA4, 0x76, 0x7B, 0xB7],
    [0xCC, 0xBB, 0x3E, 0x5A, 0xFB, 0x60, 0xB1, 0x86, 0x3B, 0x52, 0xA1, 0x6C, 0xAA, 0x55, 0x29, 0x9D],
    [0x97, 0xB2, 0x87, 0x90, 0x61, 0xBE, 0xDC, 0xFC, 0xBC, 0x95, 0xCF, 0xCD, 0x37, 0x3F, 0x5B, 0xD1],
    [0x53, 0x39, 0x84, 0x3C, 0x41, 0xA2, 0x6D, 0x47, 0x14, 0x2A, 0x9E, 0x5D, 0x56, 0xF2, 0xD3, 0xAB],
    [0x44, 0x11, 0x92, 0xD9, 0x23, 0x20, 0x2E, 0x89, 0xB4, 0x7C, 0xB8, 0x26, 0x77, 0x99, 0xE3, 0xA5],
    [0x67, 0x4A, 0xED, 0xDE, 0xC5, 0x31, 0xFE, 0x18, 0x0D, 0x63, 0x8C, 0x80, 0xC0, 0xF7, 0x70, 0x07]
]

#def cifrar_aes(matriz_Arquivo_padding, matriz_chave):


def galois_mult(a, b):
    a = int(a)
    b = int(b)
    if not (0 <= a <= 255) or not (0 <= b <= 255):
        raise ValueError(f"Valores fora do intervalo: a={a}, b={b}")

    if a == 0 or b == 0:
        return 0

    # índice para L
    log_a = L[a >> 4][a & 0x0F]  # linha = a//16, coluna = a%16
    log_b = L[b >> 4][b & 0x0F]

    log_result = (log_a + log_b) % 255

    # índice para E
    result = E[log_result >> 4][log_result & 0x0F]

    return result

def agrupar_blocos_arquivo(matriz):
    blocos = []
    for linha in matriz:
        bloco = [linha[i:i+4] for i in range(0, len(linha), 4)]
        blocos.append(bloco)
    return blocos


#### Etapa 1: Adicionar Round Key
def aplicar_add_round_key_blocos(blocos_arquivo, blocos_chave):
    aplicar_add_round_key_blocos_etapa01 = []
    for bloco_arquivo, bloco_chave in zip(blocos_arquivo, blocos_chave):
        resultado_bloco = add_round_key_etapa01(bloco_arquivo, bloco_chave)
        aplicar_add_round_key_blocos_etapa01.append(resultado_bloco)
    
    print("🔀 Etapa 1: Adicionar Round Key")
    for idx, resultado_bloco in enumerate(aplicar_add_round_key_blocos_etapa01):
        print(f"Bloco {idx+1}:")
        for linha in resultado_bloco:
            print(' '.join(f'0x{int(byte, 16):02X}' for byte in linha))
    return aplicar_add_round_key_blocos_etapa01


def add_round_key_etapa01(matriz_Arquivo, matriz_chave):
    resultado = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor_xor = int(matriz_Arquivo[i][j], 16) ^ int(matriz_chave[i][j], 16)
            linha.append(f"0x{valor_xor:02x}")
        resultado.append(linha)
    return list(zip(*resultado))


#### Etapa 2: Substituir S-Box
def substituir_Sbox_Etapa02(aplicar_add_round_key_blocos_etapa01):
    substituidas_SBox_Etapa2 = []

    # Exibe os resultados de cada bloco
    for idx, resultado in enumerate(aplicar_add_round_key_blocos_etapa01):
        for linha_idx, linha in enumerate(resultado):
            nova_linha = []
            for palavra_idx, palavra in enumerate(linha):
                palavra_int = int(palavra, 16) if isinstance(palavra, str) and palavra.startswith('0x') else palavra
                palavra_bytes = palavra_int.to_bytes(1, byteorder='big')
                nova_palavra = substituicao_palavra(palavra_bytes)
                nova_linha.append(f"0x{nova_palavra[0]:02x}")  # Armazena como string hexadecimal

            substituidas_SBox_Etapa2.append(nova_linha)
    # Exemplo de uso: mostrar a lista final
    print("\n📦 Etapa 2: Substituir S-Box")
    blocos = [substituidas_SBox_Etapa2[i:i+4] for i in range(0, len(substituidas_SBox_Etapa2), 4)]
    for idx, bloco in enumerate(blocos):
        print(f"Bloco {idx+1}:")
        for linha in bloco:
            print(' '.join(f'0x{int(byte, 16):02X}' for byte in linha))
    return substituidas_SBox_Etapa2

#### Etapa 3: Shift Rows
def shift_rows_blocos(linhas_blocos):
    blocos_shifted = []
    blocos = [linhas_blocos[i:i+4] for i in range(0, len(linhas_blocos), 4)]

    print("\n🔁 Estado após ShiftRows:")

    for idx, bloco in enumerate(blocos):
        # Aplica ShiftRows
        novo_bloco = []
        for i in range(4):
            nova_linha = bloco[i][i:] + bloco[i][:i]  # Rotaciona i posições
            novo_bloco.append(nova_linha)

        # Print formatado
        print(f"bloco {idx+1:02d}")
        for linha in novo_bloco:
            print(" ".join(linha))

        blocos_shifted.extend(novo_bloco)

    return blocos_shifted

#### Etapa 4: Mix Columns
def mix_columns_blocos(matriz_shift_rows_Etapa03):
    blocos = [matriz_shift_rows_Etapa03[i:i+4] for i in range(0, len(matriz_shift_rows_Etapa03), 4)]
    blocos_mix = []
    for idx, bloco in enumerate(blocos):
        for i in range(4):
            for j in range(4):
                if isinstance(bloco[i][j], str):
                    bloco[i][j] = int(bloco[i][j], 16)
        result = [[0] * 4 for _ in range(4)]
        mult_matrix = [
            [2, 3, 1, 1],
            [1, 2, 3, 1],
            [1, 1, 2, 3],
            [3, 1, 1, 2]
        ]

        for col in range(4):
            coluna = [bloco[linha][col] for linha in range(4)]
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

        print(f"\n🔀 Resultado após MixColumns - Bloco {idx+1}:\n")
        for linha in result:
            print(' '.join(f'0x{int(byte):02X}' for byte in linha))
        blocos_mix.extend(result)

    return blocos_mix

#### Etapa 5: Add Round Key (Etapa Final)
# Converte todos os elementos de uma matriz de '0x..' (str) para int
def converter_hex_para_int(matriz_hex):
    return [[int(x, 16) if isinstance(x, str) else x for x in linha] for linha in matriz_hex]
 

# Função para converter a chave expandida (colunas) em blocos 4x4
def construir_blocos_4x4(colunas_hex):
    blocos = []
    for i in range(0, len(colunas_hex), 4):
        bloco = []
        for linha in range(4):  # cada linha do bloco
            linha_bloco = [
                colunas_hex[i + 0][linha],
                colunas_hex[i + 1][linha],
                colunas_hex[i + 2][linha],
                colunas_hex[i + 3][linha]
            ]
            bloco.append(linha_bloco)
        blocos.append(bloco)
    return blocos

# Converter strings '0x..' para inteiros
def converter_blocos_para_inteiros(blocos_hex):
    blocos_int = []
    for bloco in blocos_hex:
        bloco_int = []
        for linha in bloco:
            linha_int = [int(valor, 16) for valor in linha]
            bloco_int.append(linha_int)
        blocos_int.append(bloco_int)
    return blocos_int


def add_round_key5_blocos(bloco_estado, bloco_chave):
    resultado = []

    for i in range(len(bloco_estado)):
        linha = []
        for j in range(len(bloco_estado[i])):
            val_estado = bloco_estado[i][j]
            val_chave = bloco_chave[i][j]
            if isinstance(val_chave, str):
                val_chave = int(val_chave, 16)
            if isinstance(val_estado, str):
                val_estado = int(val_estado, 16)
            linha.append(val_estado ^ val_chave)
        resultado.append(linha)

    # Impressão dos blocos no formato por colunas (5 blocos de 4x4)
    num_blocos = len(resultado) // 4
    for bloco_idx in range(num_blocos):
        print(f"\n🔀 Resultado após AddRoundKey - Bloco {bloco_idx + 1}:\n")
        bloco = resultado[bloco_idx * 4 : (bloco_idx + 1) * 4]

        # Impressão por colunas
        for i in range(4):  # linhas do novo formato
            linha = [bloco[j][i] for j in range(4)]
            print(' '.join(f'0x{valor:02x}' for valor in linha))

    return resultado



