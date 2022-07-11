import hashlib


def blake2b(password: str) -> str:
    """Return a sha512 hash of the given password."""
    return hashlib.blake2b(password.encode("utf-8")).hexdigest()
