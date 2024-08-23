#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
    subreddit (str): The name of the subreddit to query.
    
    Returns:
    int: The number of subscribers if valid, 0 otherwise.
    """
    # Define the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid being blocked
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # Return 0 for invalid subreddit
            return 0
    except requests.RequestException:
        # Return 0 in case of any request exceptions
        return 0

