from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="postgresql://postgres:postgres@localhost:5432/fast_api")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="1cd478679944c7aa4e88519a7ba061397591fb6a7a45c691963fa8f9f1a6bfc8")