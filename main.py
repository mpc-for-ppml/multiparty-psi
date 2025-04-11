from modules.party import Party
from modules.multiparty_psi import run_3_party_psi
from modules.crypto import encrypt, hash_to_int

def main():
    alice = Party("Party 0", ["apple", "banana", "cherry"])
    bob = Party("Party 1", ["banana", "cherry", "date"])
    carol = Party("Party 2", ["cherry", "banana", "fig"])

    intersection = run_3_party_psi(alice, bob, carol)

    print("Encrypted Intersection:", intersection)

    # Optional: reverse map for demonstration
    reverse_map = {encrypt(hash_to_int(x), alice.get_private_key()): x for x in alice.get_dataset()}
    re_encrypted_map = {encrypt(k, bob.get_private_key()): v for k, v in reverse_map.items()}
    final_map = {encrypt(k, carol.get_private_key()): v for k, v in re_encrypted_map.items()}

    result = [final_map[x] for x in intersection]
    print("Intersection:", result)

if __name__ == "__main__":
    main()
