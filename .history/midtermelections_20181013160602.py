import praw

reddit = praw.Reddit(client_id='Q8FkH2LSqlFeqg',
                     client_secret='3Fe1o1_LTgp53yijN2JU9BOqX6U ',
                     user_agent='script:midterm_data:1.0 (by /u/Luxxee)',
                     username='Luxxee',
                     password='cheyenne')

print(reddit.read_only)

subreddit = reddit.subreddit('BlueMidterm2018')

for submission in subreddit.new(limit=1000):
    print(submission.title, submission.id)
