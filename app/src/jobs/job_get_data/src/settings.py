import os
from dotenv import load_dotenv
from pathlib import Path

import MySQLdb


dotenv_path = Path('./config/prod.env')
load_dotenv(dotenv_path=dotenv_path)


HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SSL_CERT = os.getenv("SSL_CERT")


connection = MySQLdb.connect(
  host= HOST,
  user= USERNAME,
  passwd= PASSWORD,
  db= DATABASE,
  ssl      = {
    "ca": SSL_CERT
  }
)


cursor = connection.cursor()