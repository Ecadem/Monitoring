import json
import pandas as pd

from src.dependencies import (
    create_cron_instance,
)

from .src.functions import (
    job_func,
)


from .src.querys import (
    MIN_INTERVAL_QUERY,
    GET_DATA_QUERY
)

from .src.settings import (
    connection,
)

def init_job_get_data():

    interval = pd.read_sql(MIN_INTERVAL_QUERY, connection).values[0][0]

    jobs = [
        { 'args': [GET_DATA_QUERY], 'interval': interval }
    ]

    scheduler = create_cron_instance(
        jobs,
        job_func
    )
    
    return scheduler
