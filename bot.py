import telebot
import time
import random

# הכנס כאן את הנתונים שלך
TOKEN = '8872096335:AAGn1ytYA6aVelKViHZ3J2m_xw2tBU0JyWw'
CHAT_ID = '964800079'

bot = telebot.TeleBot(TOKEN)
MESSAGE = "לא לכעוס או להיות עצוב - בורא עולם דואג להכל ❤️"

def send_random_reminders():
    print("הבוט התחיל לפעול וישלח תזכורות...")
    
    while True:
        try:
            # שליחת ההודעה
            bot.send_message(CHAT_ID, MESSAGE)
            print("הודעה נשלחה בהצלחה!")
            
            # הגרלת זמן המתנה עד להודעה הבאה
            # מחשב זמן רנדומלי בין 3 שעות (10800 שניות) ל-7 שעות (25200 שניות)
            # אפשר לשנות את המספרים כדי לשנות את התדירות
            sleep_time = random.randint(10800, 25200) 
            
            hours = sleep_time // 3600
            minutes = (sleep_time % 3600) // 60
            print(f"ההודעה הבאה תישלח בעוד {hours} שעות ו-{minutes} דקות.")
            
            time.sleep(sleep_time)
            
        except Exception as e:
            print(f"אירעה שגיאה: {e}")
            # במקרה של שגיאה (למשל ניתוק אינטרנט), נחכה דקה וננסה שוב
            time.sleep(60)

if __name__ == '__main__':
    send_random_reminders()
