#!/usr/bin/python3
'''
function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
or a given subreddit
'''

import requests

def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "CustomUserAgent/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        subscribers_count = data['data']['subscribers']
        return subscribers_count
    elif response.status_code == 302:
        print(f"Subreddit '{subreddit}' is not valid.")
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0
