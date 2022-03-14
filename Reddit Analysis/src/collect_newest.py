# -*- coding: utf-8 -*-
"""
Call script as follows: python3 collect_newest.py -o <output_file> -s <subreddit>
"""

import requests
import json      ## imports
import sys

request_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

sub = sys.argv[4] ## subreddit for analysis

with open(sys.argv[2], 'w') as sample:
    
    data = []  
    url = 'https://www.reddit.com'+sub+'/new.json?limit=100'  ## url generation for subreddit
    response = requests.get(url, headers=request_headers)
    root_element = response.json()
            
    for post in root_element['data']['children']: ## access post data with API
            
        data.append(post)  ## add post to list
                
    sample.write(
            '' +
            '\n'.join(json.dumps(i) for i in data) +  ## write posts to json file for analysis by other script
            '\n')

sample.close()
