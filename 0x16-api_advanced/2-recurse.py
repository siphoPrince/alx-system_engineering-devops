#!/usr/bin/python3
"""
 a recursive function that queries the Reddit API and
 returns a list containing the titles of all hot
 articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returning the list of a hot posts titles for a given subreddit"""
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
                Safari/537.36 Edg/119.0.0.0"
    }
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(
            subreddit, after)
    try:
        response = requests.get(url, headers=header, allow_redirects=False)
        data = response.json()
        children = data.get('data').get('children')
        for post in children:
            title = post.get('data').get('title')
            hot_list.append(title)
        after = data.get('data').get('after')
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
