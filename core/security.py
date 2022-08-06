from passlib.context import CryptoContext

pwd_context = CryptoContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.has(password)

def verify_password(password: str, hash: str) -> bool:
    return pwd_context.verify_password(password, hash)