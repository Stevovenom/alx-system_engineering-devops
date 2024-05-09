#!/usr/bin/python3

"""
importing requests module
"""

from requests import get

def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("Please provide a valid subreddit name.")
        return

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)

    if response.status_code != 200:
        print("Failed to fetch data:", response.status_code)
        return

    try:
        all_data = response.json()
        raw1 = all_data.get('data', {}).get('children', [])

        for i in raw1:
            print(i.get('data', {}).get('title', 'Unknown Title'))

    except Exception as e:
        print("Error processing response:", e)
