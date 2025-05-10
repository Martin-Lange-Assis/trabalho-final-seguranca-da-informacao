
def gerar_chave(chave):
    bytes_chave = chave.split(',')
    # if (len(bytes_chave) != 16)
    matrix_chave = [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]
    cont = 0
    for i in range(0, 4):
        for j in range(0, 4):
            matrix_chave[j][i] = bytes(bytes_chave[cont])
            cont += 1
    print(chave)
    print(matrix_chave)

def expandir_chave_demais_palavras(palavras_iniciais):
    primeiro = 0
    ultimo = 3
    for _ in range(0, 10):
        palavra_nova = []
        for j in range(0, 4):
            palavra_nova.append(palavras_iniciais[primeiro][j] ^ palavras_iniciais[ultimo][j])
        primeiro += 1
        ultimo += 1
        palavras_iniciais.append(palavra_nova)
