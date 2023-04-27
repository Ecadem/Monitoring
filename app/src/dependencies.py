from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import re


def create_cron_instance(
        jobs,
        func
    ):

    scheduler = BackgroundScheduler()
    for job in jobs:
        args = job['args']
        interval = job['interval']

        scheduler.add_job(
            func,
            'interval',
            args = args,
            hours = int(interval)
        )

    return scheduler


def data_work(data):
    for i in data:
        # Color
        if i['statusCode'] == 200:
            i['statusCode'] = "#21f104"
        else:
            i['statusCode'] = "#c60000"

        # Date
        i['Recent'] = datetime.strptime(str(i['Recent']), '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%d-%m-%Y')

        # url
        try:
            i['url'] = re.search('https?://([\w.-]+\.[\w.-]+).*', i['url']).group(1)
        except:
            print(i['url'])
            
        # url photo
        if i['photoUrl'] == None:
            i['photoUrl'] = 'https://i.imgur.com/kJ00MaT.png'
    
    return data