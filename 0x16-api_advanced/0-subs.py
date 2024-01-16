#!/usr/bin/python3
'''
function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
or a given subreddit
'''

import requests
# Inside 0-subs.py
import requests

def number_of_subscribers(subreddit):
    '''
    Return the number of subreddit subscribers
    '''
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.217 Safari/537.36'

    headers = {'User-Agent': user_agent}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        print(f"Error: Unable to fetch data. Status code: {req.status_code}")
        return 0

    try:
        data = req.json()
        print("Complete JSON response:")
        print(data)  # Print the entire JSON response
        subscribers = data['data']['subscribers']
        return subscribers
    except KeyError:
        # Handle the case where the structure of the JSON response has changed
        print("Error: Unable to retrieve subscribers from JSON response.")
        return 0

