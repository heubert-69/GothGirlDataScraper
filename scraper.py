import praw
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

#Building a Data scraper for general use
reddit = praw.Reddit(
    client_id="YOUR-CLIENT-ID",
    client_secret="YOUR-SECRET-KEY",
    user_agent="YOUR-APP-NAME"
)

subreddits = ["goth", "darkromance", "AltFashion", "emo", "romance", "literature", "poet"]
post_limit = 100 #best limit for a lightweight LLM

dataset = []

for sub in subreddits:
	subreddit = reddit.subreddit(sub)
	for post in subreddit.hot(limit=post_limit):
		if post.selftext:
			dataset.append({
				"prompt": post.title.strip(),
				"response": post.selftext.strip()
			})
		post.comments.replace_more(limit=0)
		for comment in post.comments[:5]:
			if comment.body and len(comment.body) < 300:
				dataset.append({
					"prompt": post.title.strip(),
					"response": comment.body.strip()
				})
df = pd.DataFrame(dataset)
df.drop_duplicates(inplace=True)
df.to_json("goth_girl_dataset.json", orient="records", lines=True)

print(f"Saved {len(df)} conversations")
