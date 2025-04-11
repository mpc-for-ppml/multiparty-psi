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
    print("\n🔍 Intersection:", intersection)

if __name__ == "__main__":
    main()
