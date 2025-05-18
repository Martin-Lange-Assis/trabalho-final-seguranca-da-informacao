from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def aes_ecb_process(input_file, output_file, key, encrypt=True):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    padder = padding.PKCS7(128).padder() if encrypt else padding.PKCS7(128).unpadder()
    with open(input_file, 'rb') as f:
        data = f.read()
    processed = padder.update(data) + padder.finalize() if encrypt else data
    ctx = cipher.encryptor() if encrypt else cipher.decryptor()
    result = ctx.update(processed) + ctx.finalize()
    if not encrypt:
        result = padder.update(result) + padder.finalize()
    with open(output_file, 'wb') as f:
        f.write(result)

# Example usage
key = os.urandom(16)  # 128-bit key
aes_ecb_process('./files/TesteArquivo.txt', './files/encrypted-lib.bin', key, encrypt=True)
aes_ecb_process('./files/encrypted-lib.bin', './files/decrypted-lib.txt', key, encrypt=False)