# Reddit API Project

## Introduction
This project includes Python scripts that interact with the Reddit API to perform various tasks. The scripts utilize the `requests` library to make HTTP requests and parse JSON responses.

### Prerequisites
- Python 3
- `requests` library (install using `pip install requests`)

## Scripts

### 0-subs.py
This script queries the Reddit API and returns the number of subscribers for a given subreddit.

#### Usage
```bash
./0-main.py programming
1-top_ten.py
This script queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

Usage
bash
Copy code
./1-main.py programming
2-recurse.py
This recursive script queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

Usage
bash
Copy code
./2-main.py programming
100-count.py
This recursive script queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

Usage
bash
Copy code
./100-main.py programming 'python java javascript'
