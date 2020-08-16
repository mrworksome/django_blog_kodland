import os

HOST = "localhost" if "HOST" not in os.environ else os.environ.get("HOST")
PORT = 5432 if "PORT" not in os.environ else os.environ.get("PORT")
DB = "test_2" if "DB" not in os.environ else os.environ.get("DB")
DB_PASSWORD = (
    "12345" if "DB_PASSWORD" not in os.environ else os.environ.get("DB_PASSWORD")
)
DB_USER = "postgres" if "DB_USER" not in os.environ else os.environ.get("DB_USER")
