# Reddit Save Exporter

This script connects with your reddit account to extract any saved comments and submissions into an SQLite Database.

Under the hood it uses `praw` so if you want to modify this, its [docs](https://praw.readthedocs.io/en/latest/index.html) may be handy.

Note that reddit saves at most 1000 entries for you - when you try to save more, the oldest entries will be deleted.

## Instructions

1. Create a reddit app using [this form](https://www.reddit.com/prefs/apps/). Select `script`, the other settings don't matter
2. Clone the repository using `git clone https://github.com/JeftavanderHorst/reddit-save-exporter && cd reddit-save-exporter`
3. Copy `.env.example` to a new file named `.env` and fill in the environment variables
4. Install the dependencies using `pip install -r requirements.txt`
5. Run `main.py`
