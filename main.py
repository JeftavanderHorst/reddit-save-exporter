import os
import sqlite3

import praw
from dotenv import load_dotenv
from praw.models.reddit import submission, comment

load_dotenv()

sql = open('init.sql', 'r').read()
db = sqlite3.connect('saved.db')
cursor = db.cursor()
cursor.executescript(sql)

reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                     password=os.getenv("REDDIT_PASSWORD"),
                     user_agent="reddit-save-saver",
                     username=os.getenv("REDDIT_USERNAME"))

for item in reddit.user.me().saved(limit=None):
    print(item.id)
    if type(item) == submission.Submission:
        cursor.execute("INSERT INTO submissions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [
            item.id,
            item.author.name if item.author is not None else None,
            item.title,
            item.selftext if item.is_self else None,
            item.url if not item.is_self else None,
            item.permalink,
            item.score,
            item.over_18,
            item.subreddit.display_name,
            item.created_utc
        ])
    elif type(item) == comment.Comment:
        cursor.execute("INSERT INTO comments VALUES (?, ?, ?, ?, ?, ?, ?)", [
            item.id,
            item.author.name if item.author is not None else None,
            item.body,
            item.permalink,
            item.score,
            item.subreddit.display_name,
            item.created_utc
        ])
    else:
        print('unknown', type(item))

db.commit()
db.close()
