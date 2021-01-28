import csv
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_json', help = 'pass a sns json file')
args = parser.parse_args()

fieldnames = ['url', 'created_at', 'text', 'id', 'user_id','retweetedTweet']

with open(args.file_json) as f, open(args.file_json[:-4] + 'csv','w') as f2:
    writer = csv.DictWriter(f2, fieldnames=fieldnames)
    writer.writeheader()
    for line in f:
        data = json.loads(line)
        writer.writerow({'url': data['url'], 'created_at' : data['date'], 'text': data['content'], 'id': data['id'], 'user_id' : data['user']['id'], 'retweetedTweet' :data['retweetedTweet']})