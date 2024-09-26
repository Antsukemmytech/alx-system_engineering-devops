#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
"OK" if the subreddit exists, otherwise "0".
"""
import requests

def number_of_subscribers(subreddit):
    """ Queries the Reddit API to check subreddit existence """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the status code is 200 (successful response)
    if res.status_code != 200:
        return "0"

    dic = res.json()

    # Ensure the response contains data and the 'subscribers' key
    if 'data' not in dic or 'subscribers' not in dic['data']:
        return "0"
    
    # If everything is good, return "OK"
    return "OK"

