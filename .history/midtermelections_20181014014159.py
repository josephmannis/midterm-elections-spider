import praw
from requests import Session
import pandas as pd
from datetime import datetime, time, timedelta
from upload import upload_sheet, create_folder


"""
Post title
Links/body text
number of upvotes
number of downvotes
url
date posted
comments
"""

# For determining if a post from the subreddit is within the desired range


def is_yesterday(timestamp):
    midnight = datetime.combine(datetime.today(), time.min)
    yesterday_midnight = (midnight - timedelta(days=1))
    return yesterday_midnight.timestamp() <= timestamp < midnight.timestamp()

# Gets the posts for the day in the given subreddit and returns the data in a dictionary


def get_posts_for_day(subreddit):
    topics_dictionary = {"Title": [], "Score": [], "URL": [],
                         "Number of Comments": [], "Created On": [], "Body": []}

    for submission in subreddit.new(limit=None):
        if (is_yesterday(submission.created_utc)):
            topics_dictionary["Title"].append(submission.title)
            topics_dictionary["Score"].append(submission.score)
            topics_dictionary["URL"].append(submission.url)
            topics_dictionary["Number of Comments"].append(
                submission.num_comments)
            topics_dictionary["Created On"].append(submission.created)
            topics_dictionary["Body"].append(submission.selftext)

    return topics_dictionary


def parse_subreddits():
    session = Session()
    reddit = praw.Reddit(client_id='Q8FkH2LSqlFeqg',
                         client_secret='3Fe1o1_LTgp53yijN2JU9BOqX6U',
                         user_agent='script:midterm_data:1.0 (by /u/Luxxee)',
                         requestor_kwargs={'session': session},
                         username='Luxxee',
                         password='cheyenne')

    reddit.read_only = True

    # Get the ID of the folder made to store today's data
    folder_for_day = create_folder(
        str(datetime.today()), '1ab8g1EWSS1PcLibWwD83sXLGtzQds4IJ')

    # Establish Subreddits
    subreddits = ['BlueMidterm2018', 'politics',
                  'massachusettspolitics', 'mainepolitics', 'vermontpolitics']

    # For every subreddit in the list
    for sub in subreddits:
        # Get the data
        topics_dictionary = get_posts_for_day(reddit.subreddit(sub))
        # Format it
        topics_data = pd.DataFrame(topics_dictionary)
        # Export to CSV
        name = sub + str(datetime.combine(datetime.today(), time.min)) + '.csv'
        topics_data.to_csv(name, index=False)
        # Upload to drive
        upload_sheet(name, folder_for_day)
