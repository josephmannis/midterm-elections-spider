import praw
from requests import Session
import pandas as pd
import time
import datetime


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
subs = []

for submission in subreddit.new(limit=None):
    # if (submission.created_utc < (int(round(time.time() * 1000)) - 86400000)):
        # topics_dict["Title"].append(submission.title)
        # topics_dict["Score"].append(submission.score)
        # topics_dict["ID"].append(submission.id)
        # topics_dict["URL"].append(submission.url)
        # topics_dict["Number of Comments"].append(submission.num_comments)
        # topics_dict["Created On"].append(submission.created)
        # topics_dict["Body"].append(submission.selftext)\
    subs.append(submission.title)

    print(submission.title)
    print(datetime.datetime.fromtimestamp(submission.created_utc))

subs[0]
# topics_data = pd.DataFrame(topics_dict)
# topics_data.to_csv('BlueMidterm.csv', index=False)
