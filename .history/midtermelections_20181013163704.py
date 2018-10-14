import praw
from requests import Session
import pandas as pd


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

topics_dict = {"Title": [],
               "Score": [],
               "ID": [], "URL": [],
               "Number of Comments": [],
               "Created On": [],
               "Body": []}

for submission in subreddit.new(limit=None):
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
# topics_data.to_csv('BlueMidterm.csv', index=False)
