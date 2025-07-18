#!/usr/bin/python3
"""
Task: Fetch posts from JSONPlaceholder and process the data.
"""

import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print the status code + post titles."""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to retrieve posts")


def fetch_and_save_posts():
    """Fetch posts and save them into a CSV file."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        structured_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_data)

        print("Data successfully saved to posts.csv")
    else:
        print("Failed to retrieve posts")

