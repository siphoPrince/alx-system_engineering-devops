#!/usr/bin/python3
"""
 function that queries the Reddit API and prints the
 titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    headers = {'User-Agent': 'Mozilla/5.0'}  # Use a valid user-agent

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 302:
        print("Invalid subreddit. Please provide a valid subreddit.")
        return

    if req.status_code != 200:
        print(f"Error: Unable to fetch data. Status code: {req.status_code}")
        return

    try:
        data = req.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            print(title)

    except KeyError:
        print("Error: Unable to retrieve post titles from JSON response.")
