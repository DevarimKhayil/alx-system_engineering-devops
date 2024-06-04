#!/usr/bin/python3
"""
This module contains the function recurse.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list containing the titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        hot_list.extend([post['data']['title'] for post in data['data']['children']])
        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None

