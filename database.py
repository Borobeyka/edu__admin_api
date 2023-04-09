from pymongo import MongoClient
import psycopg2
import psycopg2.extras

from utils import (
    PG_HOST, PG_PORT, PG_NAME, PG_USER, PG_PASS,
    MG_HOST, MG_PORT
)


dbMG = MongoClient(f"mongodb://{MG_HOST}:{MG_PORT}/").admindb


dbPGcon = psycopg2.connect(
    dbname=PG_NAME,
    user=PG_USER,
    password=PG_PASS,
    host=PG_HOST,
    port=PG_PORT
)
dbPG = dbPGcon.cursor(cursor_factory=psycopg2.extras.DictCursor)
