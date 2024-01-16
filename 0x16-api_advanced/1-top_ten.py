#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
If the subreddit is invalid, prints None.
Usage:
    ./1-main.py programming
    ./1-main.py this_is_a_fake_subreddit
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    """ Reddit API endpoint for getting subreddit information"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

""" Set a custom User-Agent to avoid authentication issues"""
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    try:
        """ Make the GET request to the Reddit API"""
        response = requests.get(url, headers=headers)

        """ Check if the request was successful (status code 200)"""
        if response.status_code == 200:
            """Parse the JSON response"""
            data = response.json()

            """ Check if there are posts in the response"""
            if 'data' in data and 'children' in data['data']:
                """ Print the titles of the first 10 posts """
                for post in data['data']['children']:
                    print(post['data']['title'])
            else:
                print("No posts found for the subreddit.")
        elif response.status_code == 404:
            """Subreddit not found"""
            print(f"Subreddit '{subreddit}' not found.")
        else:
            """Handle other status codes if needed"""
            print(f"Error: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

""" Example usage"""
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
