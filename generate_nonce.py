import random

nonce = random.randint(0, 0xFFFFFFFF)
str_nonce = "{:08x}".format(nonce)
with open("texts/nonce.txt", "w") as file:
    file.write(str_nonce)