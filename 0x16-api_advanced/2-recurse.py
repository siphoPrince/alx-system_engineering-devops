#!/usr/bin/python3
"""
 a recursive function that queries the Reddit API and
 returns a list containing the titles of all hot
 articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetch and return the titles of
    all hot articles for a given subreddit.
    """
    if not subreddit:
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'

    headers = {'User-Agent': 'chrome 120.0.6099.217'}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 302:
        print("Invalid subreddit. Please provide a valid subreddit.")
        return None

    if req.status_code != 200:
        print(f"Error: Unable to fetch data. Status code: {req.status_code}")
        return None

    try:
        data = req.json()
        posts = data['data']['children']
        after = data['data']['after']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        if after:
            recurse(subreddit, hot_list, after)

    except KeyError:
        print("Error: Unable to retrieve post titles from JSON response.")

    return hot_list
