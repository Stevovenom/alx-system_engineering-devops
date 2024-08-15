#!/usr/bin/python3

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    If the subreddit is invalid, it prints 'None'.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        all_data = response.json()
        posts = all_data.get('data', {}).get('children', [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get('data', {}).get('title', 'None'))

    except requests.RequestException as e:
        print("None")
