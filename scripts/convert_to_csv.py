import csv
import json
#import os ? 
fieldnames = ['url', 'created_at', 'text', 'id', 'user_id']

def conv_json_csv(file1):

with open('HoldUpStopLaPeur.json') as f, open('HoldUpStopLaPeur.csv','w') as f2:
    writer = csv.DictWriter(f2, fieldnames=fieldnames)
    writer.writeheader()
    for line in f:
        data = json.loads(line)
        writer.writerow({'url': data['url'], 'created_at' : data['date'], 'text': data['content'], 'id': data['id'], 'user_id' : data['user']['id']})

