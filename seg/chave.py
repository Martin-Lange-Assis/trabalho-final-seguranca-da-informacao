
sbox = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16],
]

round_constant = {
    1: [0x01, 0x00, 0x00, 0x00],
    2: [0x02, 0x00, 0x00, 0x00],
    3: [0x04, 0x00, 0x00, 0x00],
    4: [0x08, 0x00, 0x00, 0x00],
    5: [0x10, 0x00, 0x00, 0x00],
    6: [0x20, 0x00, 0x00, 0x00],
    7: [0x40, 0x00, 0x00, 0x00],
    8: [0x80, 0x00, 0x00, 0x00],
    9: [0x1B, 0x00, 0x00, 0x00],
    10: [0x36, 0x00, 0x00, 0x00]
}

def gerar_round_keys(chave):
    round_keys = chave_para_hex(chave)

    for rodada in range(1, 11):
        geracao_primeira_palavra(round_keys, rodada)

        # Adiciona as 3 palavras faltantes (além da primeira) para completar roundkey
        geracao_demais_palavras(round_keys)
    print(round_keys)
    return round_keys

# Função para converter para hexadecimal
def chave_para_hex(chave):
    """Converte uma string de caracteres em uma matriz de valores hexadecimais."""
    # Remove vírgulas e converte a string em uma lista de caracteres
    caracteres = chave.split(",")

    # Verifica se o número de caracteres é múltiplo de 4 para formar uma matriz 4x4
    if len(caracteres) != 16:
        raise ValueError("A chave deve conter exatamente 16 caracteres.")

    # Converte cada caractere para seu valor hexadecimal e organiza em uma matriz 4x4
    matriz_hex = []
    for i in range(0, len(caracteres), 4):
        linha = []
        for c in caracteres[i:i+4]:
            try:
                # Tenta converter como número
                valor = int(c)
                linha.append(hex(valor))
            except ValueError:
                # Se falhar, trata como caractere
                if len(c) == 1:  # Se for um único caractere
                    linha.append(hex(ord(c)))
                else:
                    # Para strings que não são números nem caracteres individuais
                    raise ValueError(f"Valor inválido na chave: '{c}'")
        matriz_hex.append(linha)

    # Transpor a matriz para que as linhas se tornem colunas
    matriz_transposta = list(map(list, zip(*matriz_hex)))
    print("\nMatriz hexadecimal gerada:")
    for linha in matriz_transposta:
        print(' '.join(linha))

    return matriz_hex

def geracao_primeira_palavra(round_keys, rodada):
    primeira_rk_anterior = round_keys[-4]
    ultima_rk_anterior = round_keys[-1]

    # Converte os valores de ultima_rk_anterior para inteiros e rotaciona
    rot_word = [ultima_rk_anterior[1], ultima_rk_anterior[2], ultima_rk_anterior[3], ultima_rk_anterior[0]]
    print(f"Palavra gerada (rot_word): {rot_word}")
    
    # Substituição de bytes usando a S-Box
    palavra_subs = substituicao_palavra([int(byte, 16) for byte in rot_word])  # Converte para inteiros antes de aplicar a S-Box
    palavra_subs_hex = [f"0x{byte:02X}" for byte in palavra_subs]  # Converte de volta para hexadecimal
    print(f"Palavra gerada (substituíção de palavra pelo S-Box): {palavra_subs_hex}")
    
    # XOR com a constante de rodada
    round_contant_atual = round_constant[rodada]
    print(f"Constante de rodada atual: {round_contant_atual}")
    etapa_cinco = xor_tres_quatro(palavra_subs, round_contant_atual)
    etapa_cinco_hex = [f"0x{byte:02X}" for byte in etapa_cinco]  # Converte de volta para hexadecimal
    print(f"Palavra após XOR com 3e4: {etapa_cinco_hex}")
    
    # XOR com a primeira palavra da rodada anterior
    res = xor_cinco_rk_anterior(etapa_cinco, [int(x, 16) for x in primeira_rk_anterior])
    res_hex = [f"0x{byte:02X}" for byte in res]  # Converte de volta para hexadecimal
    print(f"XOR com a primeira palavra da rodada anterior: {res_hex}")

    round_keys.append(res_hex)

def substituicao_palavra(palavra):
    """Substitui cada byte da palavra usando a S-Box."""
    nova_palavra = []
    for byte in palavra:
        substituido = aplicar_sbox(byte)
        nova_palavra.append(substituido)
    return nova_palavra

def aplicar_sbox(byte):
    linha = (byte & 0xF0) >> 4  # 4 bits mais significativos
    coluna = byte & 0x0F       # 4 bits menos significativos
    return sbox[linha][coluna]

def xor_tres_quatro(palavra_subs, round_contant_atual):
    nova_palavra = []
    for i in range(0, len(palavra_subs)):
        nova_palavra.append(palavra_subs[i] ^ round_contant_atual[i])
    return nova_palavra

def xor_cinco_rk_anterior(etapa_cinco, primeira_rk_anterior):
    nova_palavra = []
    for i in range(0, len(etapa_cinco)):
        nova_palavra.append(etapa_cinco[i] ^ primeira_rk_anterior[i])
    return nova_palavra

def geracao_demais_palavras(round_keys):
    words_size = len(round_keys)

    primeiro = words_size - 4
    ultimo = words_size - 1

    for _ in range(0, 3): # Já temos a 1 palavra da Roundkey, geramos as outras 3
        new_word = []
        for j in range(0, 4): # Cada palavra tem 4 bytes
            int_xor_result = int(round_keys[primeiro][j], 16) ^ int(round_keys[ultimo][j], 16)
            hex_result = f"0x{int_xor_result:02X}"
            new_word.append(hex_result)
        round_keys.append(new_word) # Não quebrar loop
        primeiro += 1
        ultimo += 1

def agrupar_blocos_chave(matriz_chave):
    """Agrupa os bytes da chave em blocos de 4 palavras (cada bloco é uma lista 4x4)."""
    blocos = []
    for i in range(0, len(matriz_chave), 4):
        bloco = matriz_chave[i:i+4]
        if len(bloco) == 4:
            blocos.append(bloco)
    return blocos
