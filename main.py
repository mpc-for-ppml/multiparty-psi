from modules.party import Party
from modules.multiparty_psi import run_n_party_psi
from modules.ecc import curve
from tinyec.ec import Point

def main():
    # List of parties
    parties = [
        Party("Party 0", ["banana", "cherry"]),
        Party("Party 1", ["apple", "banana", "cherry", "date"]),
        Party("Party 2", ["cherry", "banana", "fig"]),
        Party("Party 3", ["grape", "banana", "yoo", "cherry", "plane"]),
    ]

    intersection = run_n_party_psi(parties)
    print("\n🔑 Encrypted Intersection:", intersection)

    print("\n🔍 Decrypted Intersection:")
    # Just use the first party to map back
    reverse_map = parties[0].compute_final_encrypted_items(parties)

    decrypted = []
    for pt_key in reverse_map:
        point_obj = Point(curve, pt_key[0], pt_key[1])
        if str(point_obj) in intersection:
            decrypted.append(reverse_map[pt_key])

    print(decrypted)

if __name__ == "__main__":
    main()
