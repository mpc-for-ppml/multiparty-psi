from .crypto import encrypt, hash_to_int, P
import random

class Party:
    def __init__(self, name: str, dataset: list[str]):
        self.name = name
        self.dataset = dataset
        self.priv_key = random.randint(2, P - 2)
        self.pub_set = [encrypt(hash_to_int(x), self.priv_key) for x in dataset]

    def re_encrypt(self, received_set: list[int]) -> list[int]:
        return [encrypt(x, self.priv_key) for x in received_set]

    def get_name(self):
        return self.name

    def get_dataset(self):
        return self.dataset

    def get_encrypted_set(self):
        return self.pub_set

    def get_private_key(self):
        return self.priv_key
