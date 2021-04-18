import requests
import pandas as pd
from io import StringIO
from datetime import datetime,timedelta
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    r = requests.get('https://api.thingspeak.com/users/{}/channels.json'.format(user))
    channels_json = r.json()
    for channel in channels_json['channels']:
        print(channel['id'],channel['name'])
        feed_id = channel['id']
        this_date = datetime.strptime(channel['created_at'].split('T')[0],'%Y-%m-%d')
        dfs = []
        while this_date <datetime.now():
            this_date_str = this_date.strftime('%Y-%m-%d')
            next_date_str = (this_date+timedelta(days=1)).strftime('%Y-%m-%d')
            url = ('http://api.thingspeak.com/channels/{}/feeds.csv?start={}&end={}'.
                   format(feed_id,this_date_str,next_date_str))
            r = requests.get(url)
            df = pd.read_csv(StringIO(r.text))
            if len(df)>0:
                dfs.append(df)
                print(this_date,len(df))
            this_date=this_date+timedelta(days=1)
            df_all = pd.concat(dfs)
            df_all.to_csv('{}.csv'.format(channel['name']))
