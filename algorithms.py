import random
import string

def generate_token(n: int = 100) -> str:
    s = string.ascii_letters + string.digits
    return "".join([random.choice(s) for _ in range(n)])
