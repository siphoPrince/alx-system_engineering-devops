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
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    req = requests.get(url)

    if req.status_code == 403:
        print("Error 403: Access forbidden. Check subreddit restrictions.")
        print(f"Response content: {req.content.decode('utf-8')}")
        return 0

    if req.status_code != 200:
        print(f"Error: Unable to fetch data. Status code: {req.status_code}")
        return 0

    try:
        data = req.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except KeyError:
        # Handle the case where the structure of the JSON response has changed
        print("Error: Unable to retrieve subscribers from JSON response.")
        return 0
