from hashlib import sha256

# Large safe prime
P = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def hash_to_int(value: str) -> int:
    return int(sha256(value.encode()).hexdigest(), 16) % P

def encrypt(value: int, private_key: int) -> int:
    return pow(value, private_key, P)

def modinv(a: int, p: int) -> int:
    # Modular inverse using Fermat's little theorem (P is prime)
    return pow(a, -1, p)
