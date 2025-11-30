from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import base64

def decrypt_file(input_path: str, output_path: str, key_hex: str):
    key = bytes.fromhex(key_hex)  # 32 bytes
    
    with open(input_path, 'r') as f:
        b64_data = f.read()
    
    full_data = base64.b64decode(b64_data)
    nonce = full_data[:12]
    encrypted = full_data[12:]
    
    chacha = ChaCha20Poly1305(key)
    decrypted = chacha.decrypt(nonce, encrypted, None)
    
    with open(output_path, 'wb') as f:
        f.write(decrypted)

if __name__ == '__main__':
    default_key = "e7abdcb321442c2e7c46cf245b889de168ee456315e0dda6f26e1fc3c33efefa"
    key_input = input("Key [{}]: ".format(default_key)) or default_key
    default_filename = "tools.7z"
    filename = input("Output filename [{}]: ".format(default_filename)) or default_filename
    decrypt_file('data.b64', filename, key_input)