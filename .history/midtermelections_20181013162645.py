import praw
from requests import Session

"""
Post title
Links/body text
number of upvotes
number of downvotes
url
date posted
comments
"""
session = Session()
reddit = praw.Reddit(client_id='Q8FkH2LSqlFeqg',
                     client_secret='3Fe1o1_LTgp53yijN2JU9BOqX6U',
                     user_agent='script:midterm_data:1.0 (by /u/Luxxee)',
                     requestor_kwargs={'session': session},
                     username='Luxxee',
                     password='cheyenne')

reddit.read_only = True

subreddit = reddit.subreddit('BlueMidterm2018')

topics_dict = {"title": [],
               "score": [],
               "id": [], "url": [],
               "comms_num": [],
               "created": [],
               "body": []}


for submission in subreddit.new(limit=1000):
    print(submission.title)
