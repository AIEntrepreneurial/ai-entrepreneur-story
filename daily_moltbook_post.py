# MOLTBOOK DAILY POST TASK

# This task will be executed daily to post an update to Moltbook
# Run this script once per day (not more often due to rate limits)

import subprocess
import json
import sys
import os
from datetime import datetime

def post_to_moltbook():
    # We'll execute the Node.js script to make the API call
    result = subprocess.run(['node', 'moltbook_daily_post.js'], 
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Successfully posted to Moltbook")
        # Record successful post
        with open('last_moltbook_post.txt', 'w') as f:
            f.write(datetime.now().strftime('%Y-%m-%d'))
        return True
    else:
        print(f"Failed to post: {result.stderr}")
        return False

if __name__ == "__main__":
    # Check if we already posted today
    today = datetime.now().strftime('%Y-%m-%d')
    
    try:
        with open('last_moltbook_post.txt', 'r') as f:
            last_post_date = f.read().strip()
        
        if last_post_date == today:
            print("Already posted today, skipping...")
            sys.exit(0)
    except FileNotFoundError:
        # File doesn't exist, so this is the first post
        pass
    
    # Attempt to post
    success = post_to_moltbook()
    if not success:
        print("Failed to post to Moltbook (likely due to rate limiting)")