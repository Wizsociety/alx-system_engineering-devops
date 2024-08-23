#!/usr/bin/python3
"""function is to check for the subscriber on a given reddit subreddit"""
import requests

def number_of_subcribers(subreddit):
    """return the total numnber of given subreddit"""
    url="https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "user-Agent": "linux:0x16.api.advanced:v1.0.0(by /u/bdov_)"
            }
    response=requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
