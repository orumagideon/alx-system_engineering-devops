#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, returns None.

Usage:
    ./2-main.py programming
    ./2-main.py this_is_a_fake_subreddit
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to accumulate the titles of hot articles.
        after (str): The 'after' parameter for pagination.

    Returns:
        list: A list containing the titles of hot articles, or None if no results are found.
    """
    """ Base case: subreddit is not valid"""
    if subreddit is None:
        return None

    """ Reddit API endpoint for getting hot posts in a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    """ Set a custom User-Agent to avoid authentication issues """
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    """ Include the 'after' parameter if it is provided"""
    params = {'after': after} if after else {}

    try:
        """ Make the GET request to the Reddit API"""
        response = requests.get(url, headers=headers, params=params)

        """ Check if the request was successful (status code 200)"""
        if response.status_code == 200:
            """ Parse the JSON response"""
            data = response.json()

            """Check if there are posts in the response"""
            if 'data' in data and 'children' in data['data']:
                """Append titles to the hot_list"""
                for post in data['data']['children']:
                    hot_list.append(post['data']['title'])

            """ Recursively call the function with the 'after' parameter for pagination:"""
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                """ No posts found"""
                return hot_list if hot_list else None
        elif response.status_code == 404:
            """ Subreddit not found"""
            print(f"Subreddit '{subreddit}' not found.")
            return None
        else:
            """ Handle other status codes if needed"""
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

""" Example usage"""
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        result = recurse(subreddit_name)
        if result is not None:
            print(len(result))
        else:
            print("None")
