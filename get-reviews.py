import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
key = os.getenv('API-KEY')

# set up the request parameters
params = {
  'api_key': key,
  'type': 'reviewer_profile',
  'url':'https://www.amazon.com/gp/profile/amzn1.account.AE4G4KSB4VZSLBFEACGGH3SFEPLA/ref=cm_cr_arp_d_gw_btm?ie=UTF8',
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)
# ret = json.dump(api_result.json())

names = {}

# print the JSON response from Rainforest API
with open('data.json', 'w') as outfile:
    new_name = api_result.json()['reviewer_details']['name']
    outfile.write("reviewer: " + new_name + "\n")
    names[new_name] = new_name

    for j in api_result.json()['reviews']:
        outfile.write(" \tASIN:     " + j['product']['asin'] + "\n")
        outfile.write(" \tTitle:    " + j['product']['title'] + "\n")
        outfile.write(" \tItem link:" + j['product']['link'] + "\n")

with open('names.txt', 'w') as f:
    for i in names:
        f.write(i)
