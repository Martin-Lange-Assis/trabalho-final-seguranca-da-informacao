import os

def selecionar_arquivo():
    """Solicita ao usuário o caminho do arquivo via input."""
    caminho = input("Digite o caminho completo do arquivo para ler: ")
    return caminho

def selecionar_destino():
    """Solicita ao usuário o caminho para salvar o arquivo via input."""
    caminho = input("Digite o caminho completo para salvar o arquivo: ")
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

def mostrar_bytes_em_hex(bits):
    if len(bits) % 8 != 0:
        print(f"Aviso: número de bits ({len(bits)}) não é múltiplo de 8. Truncando para exibição.")
        bits = bits[:len(bits) - (len(bits) % 8)]
    hex_data = []
    for i in range(0, len(bits), 8):
        byte_str = ''.join(bits[i:i+8])
        byte = int(byte_str, 2)
        hex_data.append(f"0x{byte:02X}")

    # Monta matriz 4 linhas por N colunas (preenchendo colunas da esquerda para a direita)
    linhas = []
    for i in range(0, len(hex_data), 4):
        linhas.append(hex_data[i:i+4])
    return linhas

def PKCS7_Padding(matriz):
    # Junta todos os elementos da matriz em uma lista única (ordem por linhas)
    flat = []
    for linha in matriz:
        flat.extend(linha)
    total = len(flat)
    # Calcula o padding necessário para completar múltiplos de 16
    resto = total % 16
    if resto == 0:
        padding = 16
    else:
        padding = 16 - resto
    # Adiciona o padding (valor em hexadecimal, ex: 0x10)
    flat.extend([f"0x{padding:02X}"] * padding)
    # Quebra em blocos de 16
    blocos = []
    for i in range(0, len(flat), 16):
        blocos.append(flat[i:i+16])
    return blocos


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

## Função para salvar o arquivo criptografado
def salvar_arquivo_criptografado(lista_plana):
    caminho_saida = './files/saidaCriptografada.bin'
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

    with open(caminho_saida, 'w', encoding='latin-1') as f:
        linha = ''.join([chr(int(hex_val, 16)) for hex_val in lista_plana])
        f.write(linha + '\n')  # salva tudo em uma única linha

    print(f"Arquivo criptografado salvo em: {caminho_saida}")

def salvar_em_arquivo(texto, caminho='./files/saidaDescriptografada.txt'):
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(texto)
        print(f"✅ Arquivo descriptografado salvo em: {caminho}")

