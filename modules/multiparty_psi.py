from .party import Party

def multi_encrypt(data: list[int], parties: list[Party], skip_party: Party) -> list[int]:
    """Encrypt data through all parties except skip_party."""
    for party in parties:
        if party != skip_party:
            data = party.re_encrypt(data)
    return data

def run_3_party_psi(p1: Party, p2: Party, p3: Party):
    # Step 1: Encrypt data by each party (done during init)

    # Step 2: Re-encrypt others' data
    p1_to_p2 = p2.re_encrypt(p1.get_encrypted_set())
    p1_final = p3.re_encrypt(p1_to_p2)

    p2_to_p3 = p3.re_encrypt(p2.get_encrypted_set())
    p2_final = p1.re_encrypt(p2_to_p3)

    p3_to_p1 = p1.re_encrypt(p3.get_encrypted_set())
    p3_final = p2.re_encrypt(p3_to_p1)

    # Step 3: Intersection of encrypted values
    intersection = set(p1_final) & set(p2_final) & set(p3_final)

    return intersection, p1_final, p2_final, p3_final

def run_n_party_psi(parties: list[Party]):
    encrypted_sets = {}

    for party in parties:
        encrypted_sets[party.get_name()] = multi_encrypt(
            party.get_encrypted_set(),
            parties,
            party
        )

    # Intersection of all encrypted sets
    final_sets = list(encrypted_sets.values())
    intersection = set(final_sets[0])
    for s in final_sets[1:]:
        intersection &= set(s)

    return intersection, encrypted_sets
