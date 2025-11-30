from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
import base64

def encrypt_file(input_path: str, output_path: str, key_hex: str):
    key = bytes.fromhex(key_hex)
    nonce = os.urandom(12)
    
    with open(input_path, 'rb') as f:
        file_data = f.read()
    
    chacha = ChaCha20Poly1305(key)
    encrypted = chacha.encrypt(nonce, file_data, None)
    full_data = nonce + encrypted
    b64_encoded = base64.b64encode(full_data).decode('ascii')
    
    with open(output_path, 'w') as f:
        f.write(b64_encoded)

if __name__ == '__main__':
    default_key = "e7abdcb321442c2e7c46cf245b889de168ee456315e0dda6f26e1fc3c33efefa"
    key_input = input("Key [{}]: ".format(default_key)) or default_key
    default_filename = "tools.7z"
    filename_input = input("File to encrypt [{}]: ".format(default_filename)) or default_filename
    encrypt_file(filename_input, 'data.b64', key_input)