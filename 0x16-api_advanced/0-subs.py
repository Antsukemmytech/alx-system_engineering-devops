#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the number of subscribers """
    u_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    
    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        # Make the request to the Reddit API with no redirects allowed
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (success)
        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers if the data is valid
            return data['data'].get('subscribers', 0)
        else:
            return 0  # Return 0 for any non-200 response (e.g., 404 or 301 redirect)
    
    except Exception as e:
        return 0  # Return 0 in case of any error
