from . import round_functions
from . import word
ROUNDS_NUMBER = 10


def salsa20_hash(input: str):
    if len(input) != 64:
        raise ValueError("Input must be 64 characters long")
    words = []
    for i in range(0, 64, 4):
        words.append(word.Word(input[i:i+4]))
    list = round_functions.doubleround(words)
    for _ in range(ROUNDS_NUMBER-1):
        list = round_functions.doubleround(list)
    result = []
    for i in range(16):
        aux_word = words[i] + list[i]
        for byte in aux_word.get_bytes_list():
            result.append(byte)
    return result


def salsa20_expand(key: str, nonce: str):
    if len(key) != 32 or len(nonce) != 16:
        raise ValueError("Key must be 32 characters long and nonce must be 16 characters long")
    constant = "expand 32-byte k"
    a = []
    for i in range(0, len(constant), 4):
        a.append(constant[i:i+4])
    k = [key[0:16], key[16:32]]
    expanded_text = a[0] + k[0] + a[1] + nonce + a[2] + k[1] + a[3]
    return salsa20_hash(expanded_text)


def salsa20(text_bytes: list[int], key: str, nonce: str):
    if len(key) != 32 or len(nonce) != 8:
        raise ValueError("Key must be 32 characters long and nonce must be 8 characters long")
    
    id = 0
    long_key = []
    while len(long_key) < len(text_bytes):
        aux_nonce = nonce + "{:08x}".format(id)
        new_key = salsa20_expand(key, aux_nonce)
        for byte in new_key:
            long_key.append(byte)
        id += 1
    long_key = long_key[:len(text_bytes)]
    
    cryptotext = []
    for i in range(len(text_bytes)):
        cryptotext.append(long_key[i] ^ text_bytes[i])
    return cryptotext