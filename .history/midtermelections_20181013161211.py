import praw
from requests import Session

session = Session()
reddit = praw.Reddit(client_id='Q8FkH2LSqlFeqg',
                     client_secret='3Fe1o1_LTgp53yijN2JU9BOqX6U ',
                     user_agent='script:midterm_data:1.0 (by /u/Luxxee)',
                     username='Luxxee',
                     password='cheyenne')

reddit.read_only = True

subreddit = reddit.subreddit('BlueMidterm2018')

for submission in subreddit.new(limit=1000):
    print(submission.title, submission.id)
