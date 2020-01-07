import hashlib


# generate hash
def create_hex_hash(username: str):
    encoded = username.encode("utf-8")
    hashed = hashlib.sha256(encoded)
    return hashed.hexdigest()

