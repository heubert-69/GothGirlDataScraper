##🦇 Goth Girl Dataset Builder
---
This Python script collects and formats Reddit posts and comments into a dataset suitable for lightweight LLM training or fine-tuning, especially for models with a dark, poetic, or emotional tone.

📌 What It Does
Scrapes hot posts and top comments from a list of subreddits related to goth, dark romance, emo, and literature.

Builds a conversational dataset with prompt–response pairs using post titles, self-texts, and short comments.

Outputs the result as a clean .jsonl file.

📂 Output Format
The dataset is saved as goth_girl_dataset.json in JSON Lines format, with each entry like:

```json
{
  "prompt": "Title of the post",
  "response": "Body of the post or comment"
}
```

🧠 Ideal For
Chatbot fine-tuning

Language models with goth/dark/romantic personality

Artistic or poetic text generation

⚙️ How It Works
```python
subreddits = ["goth", "darkromance", "AltFashion", "emo", "romance", "literature", "poet"]
post_limit = 100  # best limit for lightweight LLMs

# Loop through each subreddit
for sub in subreddits:
    for post in subreddit.hot(limit=post_limit):
        # Use post body as response if available
        # Add up to 5 short comments as additional responses
```

🛠️ Requirements
Python 3.x

pandas

praw (Python Reddit API Wrapper)

Install with:

```bash
pip install pandas praw
```

Also make sure you have a praw.ini file or provide Reddit API credentials manually.

🧪 Sample Use Case
You're building a chatbot with a gothic romantic personality. This script helps you gather ~700 conversations grounded in real user expression from niche communities — a great start for low-resource fine-tuning.

🔒 Ethical Notice
Follow Reddit API's terms of service.

Do not use this dataset for malicious, abusive, or deceptive purposes.

Respect community guidelines of scraped subreddits.

📝 Author
Built with ❤️ by Heubert-69 for Future Project Purposes
