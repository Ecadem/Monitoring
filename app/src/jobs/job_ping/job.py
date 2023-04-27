import json
import pandas as pd

from src.dependencies import (
    create_cron_instance,
)

from .src.functions import (
    ping_info,
)


from .src.querys import (
    CREATION_QUERY,
    SELECT_QUERY,
)

from .src.settings import (
    connection,
)

def init_cron_ping():

    df = pd.read_sql(SELECT_QUERY, connection)
    to_monitoring = json.loads(df.to_json(orient='records'))

    jobs = []
    for obj in to_monitoring:
        jobs.append({
            'args': [obj['id'], obj['url'], CREATION_QUERY],
            'interval': obj['intervalo']
        })


    scheduler = create_cron_instance(
        jobs,
        ping_info,
    )
    
    return scheduler
