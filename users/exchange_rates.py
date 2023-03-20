import requests
import datetime
from threading import Timer
def get_rates(): 
    params = { "format": "json"}#"words": 10, "paragraphs": 1,
    to=datetime.datetime.now().strftime('%Y-%m-%d')
    url=f'https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=100&from={to}&to={to}'
    r = requests.get(url)
    # print(r.content)
    return (r.json())
data_rates=get_rates()
print(data_rates['data']['payload'])
# def sync():

#     sync_timer=Timer(24*60*60,sync,())
#     sync_timer.start()