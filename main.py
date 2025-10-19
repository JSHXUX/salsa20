from scripts.salsa import salsa20


def main():
    secret_key = ""
    with open("texts/secret_key.txt", "r") as file:
        secret_key = file.read()
    nonce = ""
    with open("texts/nonce.txt", "r") as file:
        nonce = file.read()
    
    text = ""
    with open("texts/input.txt", "r") as file:
        text = file.read()
    input = []
    for char in text:
        input.append(ord(char))
        
    encrypted_text = salsa20(input, secret_key, nonce)
    with open("texts/encrypted.txt", "w") as file:
        for byte in encrypted_text:
            file.write(hex(byte) + " ")
    
    decrypted_text = salsa20(encrypted_text, secret_key, nonce)
    with open("texts/decrypted.txt", "w") as file:
        for byte in decrypted_text:
            file.write(chr(byte))


if __name__ == "__main__":
    main()