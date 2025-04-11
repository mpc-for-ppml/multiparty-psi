from .party import Party

def run_3_party_psi(p1: Party, p2: Party, p3: Party):
    # Step 1: Encrypt data by each party (done during init)
    parties = [p1, p2, p3]
    encrypted_sets = {}

    # Step 2: Re-encrypt others' data
    for party in parties:
        data = party.get_encrypted_set()
        for other in parties:
            if other != party:
                data = other.re_encrypt(data)
        encrypted_sets[party.get_name()] = data

    # Step 3: Compute intersection using stringified points
    final_sets = list(encrypted_sets.values())
    intersection = set(map(str, final_sets[0]))
    for s in final_sets[1:]:
        intersection &= set(map(str, s))

    return intersection

def run_n_party_psi(parties: list[Party]):
    # Step 1: Encrypt data by each party (done during init)
    encrypted_sets = {}

    # Step 2: Re-encrypt others' data
    for party in parties:
        data = party.get_encrypted_set()
        for other in parties:
            if other != party:
                data = other.re_encrypt(data)
        encrypted_sets[party.get_name()] = data

    # Step 3: Compute intersection using stringified points
    final_sets = list(encrypted_sets.values())
    intersection = set(map(str, final_sets[0]))
    for s in final_sets[1:]:
        intersection &= set(map(str, s))

    return intersection
