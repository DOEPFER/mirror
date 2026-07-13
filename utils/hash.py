import hashlib


def generate_hash(file):
    with open(file, "rb") as f:
        digest = hashlib.file_digest(f, "md5")
    return digest.hexdigest()
