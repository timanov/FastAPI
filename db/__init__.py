from .users import users
from .jobs import jobs
from .base import metadata, engine

# Создание таблиц
metadata.create_all(bind=engine)

