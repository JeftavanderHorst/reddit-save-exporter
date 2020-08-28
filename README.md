# Reddit Save Saver

This script connects with your reddit account to extract any saved comments and submissions into an SQLite Database.

Under the hood it uses `praw` so if you want to modify this, it's [docs](https://praw.readthedocs.io/en/latest/index.html) may be handy.

## Instructions

1. Create an app on `https://www.reddit.com/prefs/apps/`. Select `script`, the other settings don't matter
2. Copy `.env.example` to a new file named `.env` and fill in the environment variables
3. Install the dependencies using `pip install -U praw python-dotenv`
4. Run `main.py`
