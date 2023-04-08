from dotenv import load_dotenv
import os


load_dotenv()

PG_HOST = os.environ.get("PG_HOST")
PG_PORT = os.environ.get("PG_PORT")
PG_NAME = os.environ.get("PG_NAME")
PG_USER = os.environ.get("PG_USER")
PG_PASS = os.environ.get("PG_PASS")

MG_HOST = os.environ.get("MG_HOST")
MG_PORT = os.environ.get("MG_PORT")