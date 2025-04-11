import random
from hashlib import sha256

# Prime modulus for group (use a large safe prime in production)
P = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def hash_to_int(value):
    return int(sha256(value.encode()).hexdigest(), 16) % P

def encrypt(value, private_key):
    return pow(value, private_key, P)

def decrypt(value, private_key_inv):
    return pow(value, private_key_inv, P)

def modinv(a, p):
    # Modular inverse using Extended Euclidean Algorithm
    return pow(a, -1, p)

class Party:
    def __init__(self, name, dataset):
        self.name = name
        self.dataset = dataset
        self.priv_key = random.randint(2, P - 2)
        self.pub_set = [encrypt(hash_to_int(x), self.priv_key) for x in dataset]

    def re_encrypt(self, received_set):
        return [encrypt(x, self.priv_key) for x in received_set]

    def __str__(self):
        return f"{self.name} with set {self.dataset}"

# Sample datasets
alice = Party("Alice", ["apple", "banana", "cherry"])
bob = Party("Bob", ["banana", "cherry", "date"])
carol = Party("Carol", ["cherry", "banana", "fig"])

# Phase 1: All parties encrypt their own datasets (done in init)

# Phase 2: Encrypt each other's data
# Alice sends to Bob → Bob re-encrypts Alice’s data
alice_to_bob = bob.re_encrypt(alice.pub_set)

# Then Bob sends that to Carol → Carol re-encrypts again
alice_final = carol.re_encrypt(alice_to_bob)

# Repeat for Bob and Carol
bob_to_carol = carol.re_encrypt(bob.pub_set)
bob_final = alice.re_encrypt(bob_to_carol)

carol_to_alice = alice.re_encrypt(carol.pub_set)
carol_final = bob.re_encrypt(carol_to_alice)

# Now all parties have everyone's fully encrypted sets
# Compute intersection of encrypted values
intersection = set(alice_final) & set(bob_final) & set(carol_final)

# To reveal actual values (optional), each party maps back to input set
print("Encrypted Intersection:", intersection)

# Map back to original strings (for demo only)
reverse_map = {encrypt(hash_to_int(x), alice.priv_key): x for x in alice.dataset}
re_encrypted_reverse_map = {encrypt(k, bob.priv_key): v for k, v in reverse_map.items()}
final_reverse_map = {encrypt(k, carol.priv_key): v for k, v in re_encrypted_reverse_map.items()}

# Display intersection
result = [final_reverse_map[x] for x in intersection]
print("Intersection:", result)
