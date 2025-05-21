# trabalho-final-seguranca-da-informacao.py
# Alunos: André Heller, Luigi Garcia Marchetti e Martin Lange de Assis
# Professor: Gilvan Justino | Instituição: FURB

from chave import *
from abrir_salvar_Arquivo import *
from cifrar import *
from decifrar import *

chave = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P'

matriz_chave = gerar_round_keys(chave)
blocos_chave = agrupar_blocos_chave(matriz_chave)
print(f"\n🔒 agrupar_blocos_chave {blocos_chave} ")

operacao = int(input('Selecione a operação desejada: \n 0 - Cifrar \n 1 - Decifrar\n'))
print('Operação escolhida: ' + str(operacao))

if operacao == 0:
    print('Cifrar')
    caminho = selecionar_arquivo()
    if caminho:
        print(f"Arquivo selecionado: {caminho}")
        bits = arquivo_para_bits(caminho)
        print(f"{len(bits)} bits lidos do arquivo.")

        matriz_Arquivo = mostrar_bytes_em_hex(bits)
        matriz_Arquivo_padding = PKCS7_Padding(matriz_Arquivo)
        print(f"\n🔒 matriz_Arquivo_padding {matriz_Arquivo_padding} ")

        blocos_arquivo = agrupar_blocos_arquivo(matriz_Arquivo_padding)
        print(f"\n🔒 agrupar_blocos_arquivo {blocos_arquivo} ")

        etapa1 = aplicar_add_round_key_blocos(blocos_arquivo, blocos_chave)
        etapa2 = substituir_Sbox_Etapa02(etapa1)
        etapa3 = shift_rows_blocos(etapa2)
        etapa4 = mix_columns_blocos(etapa3)
        etapa5 = add_round_key5_blocos(etapa4, matriz_chave)

        resultado_final = [
            [f"0x{byte:02X}" if isinstance(byte, int) else byte for byte in linha]
            for linha in etapa5
        ]
        resultado_flat = [byte for linha in resultado_final for byte in linha]
        print(f"\n🔒 resultado_addroundkey_Etapa05 {resultado_final} ")

        salvar_arquivo_criptografado(resultado_flat)

else:
    print('Decifrar')
    caminho = selecionar_arquivo()
    if caminho:
        print(f"Arquivo selecionado: {caminho}")
    bits = arquivo_para_bits(caminho)
    bits = [bit for bit in bits if bit != 0x0A]
    print(f"{len(bits)} bits lidos do arquivo.")

    matriz_Arquivo = mostrar_bytes_em_hex(bits)
    dados_filtrados = [x for linha in matriz_Arquivo for x in linha if x not in ('0x0A', '0x0D')]
    blocos_arquivo = [dados_filtrados[i:i+4] for i in range(0, len(dados_filtrados), 4)]
    print(f"\n🔒 Bloco após filtro e reagrupamento: {blocos_arquivo}")

    etapa1 = inv_add_round_key5_blocos(blocos_arquivo, matriz_chave)
    etapa2 = inv_mix_columns_blocos(etapa1)
    etapa3 = inv_shift_rows_blocos(etapa2)
    etapa4 = inv_substituir_Sbox_Etapa02(etapa3)
    print(f"\n🔒 resultado_inv_substituir_Sbox_Etapa02 {etapa4} ")

    ### ate aqui esta certo depois de inv_substituir_Sbox_Etapa02 não da o resultado esperado

    
    etapa5 = inv_add_round_key1_blocos(etapa4, blocos_chave)

    blocos_4x4 = dividir_em_blocos_4x4(etapa5)  # Agora são 2 blocos 4x4 (cada bloco com 4 linhas de 4 bytes)

    print(f"🔒 resultado_inv_add_round_key (2 blocos 4x4): {blocos_4x4}")

    # Novas etapas para reconstrução do texto
    blocos_4x4 = dividir_em_blocos_4x4(etapa5)
    bloco_linear = linearizar_blocos(blocos_4x4)
     #[[['0x44', '0x45', '0x53', '0x45'], ['0x4E', '0x56', '0x4F', '0x4C'], ['0x56', '0x49', '0x4D', '0x45'], ['0x4E', '0x54', '0x4F', '0x21']],
    #  [['0x10', '0x10', '0x10', '0x10'], ['0x10', '0x10', '0x10', '0x10'], ['0x10', '0x10', '0x10', '0x10'], ['0x10', '0x10', '0x10', '0x10']]]
    
    bloco_sem_padding = remover_PKCS7_padding(bloco_linear)
    #[[['0x44', '0x45', '0x53', '0x45'], ['0x4E', '0x56', '0x4F', '0x4C'], ['0x56', '0x49', '0x4D', '0x45'], ['0x4E', '0x54', '0x4F', '0x21']],
    texto_final = ''.join(chr(int(byte, 16)) for byte in bloco_sem_padding)
    print("🔍 Bloco linear após remoção do padding:", bloco_sem_padding)
    print("✅ Texto descriptografado:", texto_final)

    with open('./files/saidaDescriptografada.txt', 'w', encoding='utf-8') as f:
        f.write(texto_final)
    print("✅ Arquivo descriptografado salvo em: ./files/saidaDescriptografada.txt")

    #🔒 resultado_inv_substituir_Sbox_Etapa02 [['0x05', '0x0b', '0x1f', '0x03'], ['0x07', '0x10', '0x03', '0x1a'], ['0x10', '0x08', '0x06', '0x00'], 
    # ['0x01', '0x04', '0x09', '0x71'], ['0x7f', '0x3a', '0x73', '0x3e'],
    #  ['0xd6', '0x90', '0xda', '0x94'], ['0x00', '0x47', '0x0c', '0x43'], ['0xb7', '0xff', '0xb3', '0xe3']]

    #[[['0x44', '0x45', '0x53', '0x45'], ['0x4E', '0x56', '0x4F', '0x4C'], ['0x56', '0x49', '0x4D', '0x45'], ['0x4E', '0x54', '0x4F', '0x21']],
    #  [['0x10', '0x10', '0x10', '0x10'], ['0x10', '0x10', '0x10', '0x10'], ['0x10', '0x10', '0x10', '0x10'], ['0x10', '0x10', '0x10', '0x10']]]
