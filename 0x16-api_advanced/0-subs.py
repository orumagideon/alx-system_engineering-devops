#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Reddit API endpoint for getting subreddit information"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    """ Set a custom User-Agent to avoid authentication issues"""
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    try:
        """ Make the GET request to the Reddit API"""
        response = requests.get(url, headers=headers)

        """ Check if the request was successful (status code 200)"""
        if response.status_code == 200:
            """ Parse the JSON response"""
            data = response.json()

            """Extract and return the number of subscribers"""
            return data['data']['subscribers']
        elif response.status_code == 404:
            """ Subreddit not found"""
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
"""Handle other status codes if needed"""
            print(f"Error: {response.status_code}")
            return 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

"""
    Example usage
"""
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print(f"Subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
