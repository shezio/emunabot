import telebot
import os
import random
from datetime import datetime, timezone

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

bot = telebot.TeleBot(TOKEN)
MESSAGE = "לא לכעוס או להיות עצוב - בורא עולם דואג להכל ❤️"

if __name__ == '__main__':
    now = datetime.now(timezone.utc)

    # Saturday = weekday 5
    if now.weekday() == 5:
        print("שבת - לא שולחים הודעות היום.")
        raise SystemExit(0)

    # Seed with today's date so all hourly runs agree on the same send-hours
    rng = random.Random(int(now.strftime('%Y%m%d')))
    num_messages = rng.randint(3, 10)
    # Hours 7-22 UTC  (= roughly 10:00-01:00 Israel time)
    send_hours = sorted(rng.sample(range(7, 23), num_messages))

    if now.hour in send_hours:
        try:
            bot.send_message(CHAT_ID, MESSAGE)
            print(f"הודעה נשלחה! שעה {now.hour} UTC (שעות היום: {send_hours})")
        except Exception as e:
            print(f"אירעה שגיאה: {e}")
            raise
    else:
        print(f"שעה {now.hour} UTC - לא שולחים עכשיו. שעות שליחה היום: {send_hours}")
