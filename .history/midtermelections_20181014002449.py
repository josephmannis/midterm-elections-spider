import praw
from requests import Session
import pandas as pd
from datetime import datetime, time, timedelta


"""
Post title
Links/body text
number of upvotes
number of downvotes
url
date posted
comments
"""

# Run every day at midnight
session = Session()
reddit = praw.Reddit(client_id='Q8FkH2LSqlFeqg',
                     client_secret='3Fe1o1_LTgp53yijN2JU9BOqX6U',
                     user_agent='script:midterm_data:1.0 (by /u/Luxxee)',
                     requestor_kwargs={'session': session},
                     username='Luxxee',
                     password='cheyenne')

reddit.read_only = True

subreddits = ['BlueMidterm2018', 'politics',
              'massachusettspolitics', 'mainepolitics', 'vermontpolitics']


def is_yesterday(timestamp):
    midnight = datetime.combine(datetime.today(), time.min)
    yesterday_midnight = (midnight - timedelta(days=1))
    return yesterday_midnight.timestamp() <= timestamp < midnight.timestamp()


def get_posts_for_day(subreddit):
    for submission in subreddit.new(limit=None):
        if (is_yesterday(submission.created_utc)):
            topics_dict["Title"].append(submission.title)
            topics_dict["Score"].append(submission.score)
            topics_dict["ID"].append(submission.id)
            topics_dict["URL"].append(submission.url)
            topics_dict["Number of Comments"].append(submission.num_comments)
            topics_dict["Created On"].append(submission.created)
            topics_dict["Body"].append(submission.selftext)


for sub in subreddits:
    topics_dict = {"Title": [],
                   "Score": [],
                   "ID": [], "URL": [],
                   "Number of Comments": [],
                   "Created On": [],
                   "Body": []}

    get_posts_for_day(reddit.subreddit(sub))
    topics_data = pd.DataFrame(topics_dict)
    topics_data.to_csv(
        'sub_' + datetime.combine(datetime.today(), time.min) + '.csv', index=False)
