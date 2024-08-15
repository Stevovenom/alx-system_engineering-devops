#!/usr/bin/python3

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    If the subreddit is invalid, it prints 'None'.
    """

    # Check if the subreddit is None or not a string
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    # Construct the API URL and headers
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}

    try:
        # Make the GET request to the Reddit API with no redirects allowed
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        # Check if the response status code is not 200 (success)
        if response.status_code != 200:
            print("None")
            return

        # Parse the JSON response
        all_data = response.json()
        posts = all_data.get('data', {}).get('children', [])

        # Check if the posts list is empty or missing
        if not posts:
            print("None")
            return

        # Loop through the posts and print each title
        for post in posts:
            print(post.get('data', {}).get('title', 'None'))

    except requests.RequestException:
        # Print 'None' if there's a network-related error
        print("None")
