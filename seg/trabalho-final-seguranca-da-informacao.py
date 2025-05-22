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


    def dividir_em_blocos_4x4_formatado(matriz):
        # Transpor: linhas viram colunas
        transposta = [list(col) for col in zip(*matriz)]  # 4 linhas, N colunas

        num_colunas = len(transposta[0])
        if num_colunas % 4 != 0:
            raise ValueError("Número de colunas da transposta deve ser múltiplo de 4")

        blocos = []
        for i in range(0, num_colunas, 4):
            bloco = []
            for j in range(4):  # para cada linha da transposta (são 4)
                linha = [transposta[j][i + k] for k in range(4)]  # monta linha por colunas
                bloco.append(linha)
            blocos.append(bloco)

        return blocos

    etapa4 = dividir_em_blocos_4x4_formatado(etapa4)
    print(f"🔒 resultado_estado: {etapa4}")
    print(f"🔒 resultado_chave: {blocos_chave}")

    etapa5 = inv_add_round_key1_blocos(etapa4, blocos_chave)

    print(f"🔒 etapa5 xor: {etapa5}")

    bloco_sem_padding = remover_PKCS7_padding_blocos(etapa5)
    print("🔒 Bloco sem padding:", bloco_sem_padding)

    bloco = achatar_blocos(bloco_sem_padding)

    texto = converter_hex_para_texto(bloco)

    print("🔒 Texto convertido:", texto)

    salvar_em_arquivo(texto)

    


    

  