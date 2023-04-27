import json
import os
from dotenv import load_dotenv
from pathlib import Path

import MySQLdb


dotenv_path = Path('./config/prod.env')
load_dotenv(dotenv_path=dotenv_path)


import pandas as pd

def job_func(
            GET_DATA_QUERY, 
            HOST = os.getenv("HOST"),
            DATABASE = os.getenv("DATABASE"),
            USERNAME = os.getenv("USERNAME"),
            PASSWORD = os.getenv("PASSWORD"),
            SSL_CERT = os.getenv("SSL_CERT")
        ):

        connection = MySQLdb.connect(
            host = HOST,
            user = USERNAME,
            passwd = PASSWORD,
            db = DATABASE,
            ssl = {
                "ca": SSL_CERT
            }
        )
        
        data = pd.read_sql(GET_DATA_QUERY, connection) 
        
        resp = json.loads( 
            data.to_json(orient='records',
                        date_format = "iso")
        )

        if resp:
            with open('src/data/ping_info.json', 'w') as outfile:
                json.dump(resp, outfile)


        connection.close()



