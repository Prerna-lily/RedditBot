# Reddit AI Content Bot

This Python script generates content for Reddit posts using Groq AI and posts it to a specified subreddit on Reddit. It utilizes the `praw` library for Reddit authentication and posting, and the `groq` library for generating AI-based content. The bot is designed to automatically generate and submit a daily post to Reddit.

## Features

- Authenticate with Reddit using the PRAW library.
- Generate AI-based content using the Groq API.
- Post generated content to a specific Reddit subreddit.
- Logs actions such as authentication, content generation, and posting.

## Requirements

Before running the script, you need to install the required libraries.

```bash
pip install praw groq
