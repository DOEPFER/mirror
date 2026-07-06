import hashlib


def generate_hash(file):
    md5h = hashlib.md5()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5h.update(chunk)
    return md5h.hexdigest()
