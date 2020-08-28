DROP TABLE IF EXISTS comments;
CREATE TABLE comments
(
    id          VARCHAR(255) PRIMARY KEY,
    author      VARCHAR(255),
    body        TEXT,
    permalink   TEXT,
    score       INT,
    subreddit   VARCHAR(255),
    created_utc TIMESTAMP
);

DROP TABLE IF EXISTS submissions;
CREATE TABLE submissions
(
    id          VARCHAR(255) PRIMARY KEY,
    author      VARCHAR(255),
    title       TEXT,
    selftext    TEXT,
    url         TEXT,
    permalink   TEXT,
    score       INT,
    over_18     BOOLEAN,
    subreddit   VARCHAR(255),
    created_utc TIMESTAMP
);
