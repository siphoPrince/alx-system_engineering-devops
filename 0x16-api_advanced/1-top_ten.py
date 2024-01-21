#!/usr/bin/python3
"""
 function that queries the Reddit API and prints the
 titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Printing the titles of the first 10 hot posts for a given subreddit"""
    import requests

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
                Safari/537.36 Edg/119.0.0.0"
    }
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    try:
        response = requests.get(url, headers=header, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data').get('children')
            if posts:
                for post in posts:
                    title = post.get('data').get('title')
                    print(title)
                return
    except Exception:
        pass
