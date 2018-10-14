import praw

reddit = praw.Reddit(client_id='Q8FkH2LSqlFeqg',
                     client_secret='3Fe1o1_LTgp53yijN2JU9BOqX6U ',
                     user_agent='script:midterm_data:1.0 (by /u/Luxxee',
                     username='luxxee',
                     password='cheyenne')

subreddit = reddit.subreddit('Nootropics')
