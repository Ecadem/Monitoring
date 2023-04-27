import os
from dotenv import load_dotenv
from pathlib import Path

import MySQLdb


dotenv_path = Path('./config/prod.env')
load_dotenv(dotenv_path=dotenv_path)


from datetime import datetime
import time
import requests

def ping_info(
            id_, 
            url, 
            CREATION_QUERY, 
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

        cursor = connection.cursor()
        
        start = time.time()
        r = requests.get(url)
        end = time.time() - start

        results = {
            'id': id_, 
            'last_update': datetime.now(),
            'time': round(end, 2), #round to 2 decimals
            'status': r.status_code 
            
        }

        query = CREATION_QUERY.format(
            results['id'],
            results['last_update'],
            results['time'],
            results['status']
        )

        cursor.execute(query)
        connection.commit()
        connection.close()



