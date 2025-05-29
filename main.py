# main.py

import time
from config import *
from datetime import datetime
from ai_generator import generate_script
from tts_engine import generate_voiceover
from tiktok_poster import post_to_tiktok
from telegram_notify import send_telegram_message

def run_bot():
    try:
        topic = get_trending_topic()
        prompt = PROMPT_TEMPLATE.format(topic=topic)
        
        print("[AI] Generating script...")
        script = generate_script(prompt)

        print("[Voice] Creating voiceover...")
        audio_path = generate_voiceover(script)

        print("[Post] Uploading to TikTok...")
        post_to_tiktok(script, audio_path)

        send_telegram_message(f"✅ TikTok posted for topic: {topic} at {datetime.now()}")

    except Exception as e:
        send_telegram_message(f"❌ Bot failed: {e}")
        print("[ERROR]", e)

if __name__ == "__main__":
    while True:
        run_bot()
        print(f"[Sleep] Waiting {INTERVAL_SECONDS} seconds...")
        time.sleep(INTERVAL_SECONDS)
      
