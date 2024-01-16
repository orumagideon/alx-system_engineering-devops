#!/usr/bin/python3
"""
Recursive function to query the Reddit API, parse titles, and print a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses titles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): The 'after' parameter for pagination.
        counts (dict): A dictionary to store word counts.

    Returns:
        None
    """
    if subreddit is None or (after is not None and after == 'null'):
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()

            if counts is None:
                counts = {}

            if 'data' in data and 'children' in data['data']:
                for post in data['data']['children']:
                    title = post['data']['title'].lower()
                    for word in word_list:
                        word = word.lower()
                        if word in title:
                            counts[word] = counts.get(word, 0) + title.count(word)

                count_words(subreddit, word_list, data['data']['after'], counts)
            else:
                print_counts(counts)
        elif response.status_code == 404:
            print("None")
        else:
            print(f"Error: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def print_counts(counts):
    if counts:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_counts:
            print(f"{word}: {count}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit_name = sys.argv[1]
        keyword_list = [x for x in sys.argv[2].split()]
        count_words(subreddit_name, keyword_list)
