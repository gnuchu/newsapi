import requests
import os
import yaml
import json


if os.name == 'posix':
  homepath = os.environ['HOME']
elif os.name == 'nt':
  homepath = "C:/Users/johng"
else:
  raise('OS not supported')

secrets_path = homepath + '/secrets/.secrets.yaml' 

with open(secrets_path) as f:
  secrets = yaml.load(f, Loader=yaml.FullLoader)#

apikey = secrets['newsapi']['apikey']

endpoint='top-headlines'
country='gb'

url = f"https://newsapi.org/v2/{endpoint}?country={country}&apiKey={apikey}"
resp = requests.get(url)

if resp.status_code == 200:
  news_j = json.loads(resp.text)
  for article in news_j['articles']:
    print(article['title'])
else:
  print(f"Error getting {url}")