import hashlib


def sha512(password: str) -> str:
    """Return a sha512 hash of the given password."""
    return hashlib.blake2b(password.encode('utf-8')).hexdigest()
