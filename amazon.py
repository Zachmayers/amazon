import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
key = os.getenv('API-KEY')

# set up the request parameters
params = {
  'api_key': key,
  'type': 'reviews',
  'amazon_domain': 'amazon.com',
  'asin': 'B08D5Z39WY',
  'review_stars': 'five_star',
  'sort_by': 'most_recent'
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)
# ret = json.dump(api_result.json())


# print the JSON response from Rainforest API
with open('data.json', 'w') as outfile:
    for i in api_result.json()['reviews']:
        outfile.write(i['profile']['name'] + "\n\t URL >  " + i['profile']['link'] + "\n\n")
