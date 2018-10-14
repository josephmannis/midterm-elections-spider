import praw
from requests import Session
import pandas as pd
from datetime import datetime, time, timedelta
import ScraperUploader


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

# Establish Subreddits
subreddits = ['BlueMidterm2018', 'politics',
              'massachusettspolitics', 'mainepolitics', 'vermontpolitics']

# Get the ID of the folder made to store today's data
folder_for_day = ScraperUploader.create_folder(
    str(datetime.today()), '1ab8g1EWSS1PcLibWwD83sXLGtzQds4IJ')


def is_yesterday(timestamp):
    midnight = datetime.combine(datetime.today(), time.min)
    yesterday_midnight = (midnight - timedelta(days=1))
    return yesterday_midnight.timestamp() <= timestamp < midnight.timestamp()


def get_posts_for_day(subreddit):
    topics_dictionary = {"Title": [], "Score": [], "ID": [], "URL": [],
                         "Number of Comments": [], "Created On": [], "Body": []}

    for submission in subreddit.new(limit=None):
        if (is_yesterday(submission.created_utc)):
            topics_dictionary["Title"].append(submission.title)
            topics_dictionary["Score"].append(submission.score)
            topics_dictionary["ID"].append(submission.id)
            topics_dictionary["URL"].append(submission.url)
            topics_dictionary["Number of Comments"].append(
                submission.num_comments)
            topics_dictionary["Created On"].append(submission.created)
            topics_dictionary["Body"].append(submission.selftext)

    return topics_dictionary


for sub in subreddits:
    topics_dictionary = get_posts_for_day(reddit.subreddit(sub))
    topics_data = pd.DataFrame(topics_dictionary)
    topics_data.to_csv(
        sub + str(datetime.combine(datetime.today(), time.min)) + '.csv', index=False)


#
