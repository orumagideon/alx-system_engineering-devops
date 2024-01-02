#!/usr/bin/python3
"""This script utilizes a REST API to retrieve progress details from a TODO list associated with a specific employee ID."""
import requests as r
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    usr_id = r.get(url + 'users/{}'.format(sys.argv[1])).json()
    to_do = r.get(url + 'todos', params={'userId': sys.argv[1]}).json()
#    print(to_do)
    completed = [title.get("title") for title in to_do if
                 title.get('completed') is True]
    print(completed)
    print("Employee {} has completed tasks({}/{}):".format(usr_id.get("name"),
                                                          len(completed),
                                                          len(to_do)))
    [print("\t {}".format(title)) for title in completed]
