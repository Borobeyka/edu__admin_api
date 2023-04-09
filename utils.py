from dotenv import load_dotenv
import os


load_dotenv()

PG_HOST = os.environ.get("POSTGRES_HOST")
PG_PORT = os.environ.get("POSTGRES_PORT")
PG_NAME = os.environ.get("POSTGRES_DB")
PG_USER = os.environ.get("POSTGRES_USER")
PG_PASS = os.environ.get("POSTGRES_PASSWORD")

MG_HOST = os.environ.get("MONGO_INITDB_HOST")
MG_PORT = os.environ.get("MONGO_INITDB_PORT")
