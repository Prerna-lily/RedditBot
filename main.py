import os
import praw
import logging
from groq import Groq

# Set up logging
logging.basicConfig(level=logging.INFO, filename='reddit_bot.log')

# Reddit API authentication
def authenticate_reddit():
    reddit = praw.Reddit(
        client_id='',
        client_secret='',
        user_agent='Chatbot by EquipmentCivil5912',
        username='',
        password=''
    )
    logging.info("Reddit authentication successful.")
    return reddit

# Generate content using Groq AI
def generate_content():
    try:
        # Pass the API key directly if not using environment variables
        api_key = "api_key"
        client = Groq(api_key=api_key)

        # Generate content using the Groq AI client
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": "Generate a daily post for Reddit"}
            ],
            model="llama-3.3-70b-versatile"
        )
        content = chat_completion.choices[0].message.content
        logging.info("Content generated successfully.")
        return content
    except Exception as e:
        logging.error(f"Error generating content: {e}")
        return None

# Post content to Reddit
def post_to_reddit(reddit, content):
    try:
        subreddit_name = 'test'  # Replace with your subreddit name
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit(title="Daily AI Post", selftext=content)
        logging.info(f"Post submitted successfully to r/{subreddit_name}.")
    except Exception as e:
        logging.error(f"Error posting to Reddit: {e}")

# Post content immediately
def post_now():
    reddit = authenticate_reddit()
    content = generate_content()
    if content:
        post_to_reddit(reddit, content)
    else:
        logging.error("No content generated. Skipping post.")

# Execute post now
if __name__ == "__main__":
    post_now()
