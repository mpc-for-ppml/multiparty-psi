from .party import Party

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

    return intersection
