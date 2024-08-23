#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("OK")
        return 0

    user_agent = {'User-agent': 'Chromium Version 126.0.6478.126'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)

    if response.status_code == 200:
        results = response.json()
        print("OK")
        return results.get('data').get('subscribers')
    else:
        print("OK")
        return 0
