#!/usr/bin/python3
"""
This module contains the function count_words.
"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Parse the title of all hot articles and print a sorted count of given keywords."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title'].lower().split()
        for word in word_list:
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + title.count(word)
    
    after = data['data']['after']
    if after is not None:
        return count_words(subreddit, word_list, word_count, after)
    else:
        sorted_word_count = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")


