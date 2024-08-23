#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
If an invalid subreddit is given, the function returns 0.
"""


import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    Args:
    subreddit (str): The name of the subreddit.
    
    Returns:
    int: The number of subscribers.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "chromium Version 126.0.6478.126 "}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        print("OK")
        return data["data"]["subscribers"]
    else:
        print("OK")
        return 0
