# Alunos: André Heller, Luigi Garcia Marchetti e Martin Lange de Assis
# Professor: Gilvan Justino
# Instituição: FURB

import ipywidgets as widgets
from IPython.display import display, clear_output
import pandas as pd
import numpy as np
import io
import cv2
import matplotlib.pyplot as plt

operacao = int(input('Selecione a operação desejada: \n 0 - Cifrar \n 1 - Decifrar \n'))
print('Operação escolhida: ' + str(operacao))

if operacao == 0:
    print('Cifrar')
else:
    print('Decifrar')

upload = widgets.FileUpload(
    accept='',  # aceita qualquer tipo
    multiple=False
)
output = widgets.Output()

def tratar_upload(change):
    with output:
        clear_output()
        for nome, arquivo in upload.value.items():
            conteudo = arquivo['content']
            print(f"📁 Nome do arquivo: {nome}")
            print(f"📏 Tamanho: {len(conteudo)} bytes")

            if nome.endswith(('.txt', '.md', '.py')):
                print("📝 Conteúdo (texto):")
                print(conteudo.decode('utf-8'))

            elif nome.endswith('.csv'):
                print("📊 Conteúdo (CSV):")
                df = pd.read_csv(io.BytesIO(conteudo))
                display(df.head())

            elif nome.endswith(('.jpg', '.jpeg', '.png')):
                print("🖼️ Imagem carregada:")
                np_array = np.frombuffer(conteudo, np.uint8)
                img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
                plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                plt.axis('off')
                plt.show()
                tratar_upload.conteudo = img

            else:
                print("📦 Arquivo carregado, mas tipo não reconhecido para visualização automática.")

            tratar_upload.raw_bytes = conteudo
            tratar_upload.nome = nome

display(upload, output)
upload.observe(tratar_upload, names='value')
