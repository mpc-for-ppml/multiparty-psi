from modules.party import Party
from modules.multiparty_psi import run_n_party_psi
from modules.crypto import encrypt, hash_to_int

def main():
    # List of parties
    parties = [
        Party("Party 0", ["apple", "banana", "cherry"]),
        Party("Party 1", ["banana", "cherry", "date"]),
        Party("Party 2", ["cherry", "banana", "fig"]),
        Party("Party 3", ["grape", "banana", "cherry"]),
    ]

    intersection, _ = run_n_party_psi(parties)

    print("Encrypted Intersection:", intersection)

    # Use the first party to reverse map just for demonstration
    first = parties[0]
    reverse_map = {encrypt(hash_to_int(x), first.get_private_key()): x for x in first.get_dataset()}

    # Re-encrypt with all others to match intersection
    for other in parties:
        if other != first:
            reverse_map = {encrypt(k, other.get_private_key()): v for k, v in reverse_map.items()}

    result = [reverse_map[x] for x in intersection]
    print("Intersection:", result)

if __name__ == "__main__":
    main()
