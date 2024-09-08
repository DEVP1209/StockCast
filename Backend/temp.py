import schedule
import time
from datetime import datetime
import logging

logging.basicConfig(filename='schedule_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def remind_me(message):
    logging.info(f"Reminder: {message}")
    print(f"Reminder: {message}")

def set_daily_standup():
    schedule.every().day.at("09:00").do(remind_me, message="Daily Standup Meeting in 15 minutes")

def set_monday_wednesday_sessions():
    schedule.every().monday.at("11:00").do(remind_me, message="Monday Session in 1 hour")
    schedule.every().wednesday.at("11:00").do(remind_me, message="Wednesday Session in 1 hour")

def set_friday_project_review():
    schedule.every().friday.at("15:00").do(remind_me, message="Project Review in 45 minutes")

def set_gym_sessions():
    schedule.every().tuesday.at("18:30").do(remind_me, message="Gym Session in 1 hour")
    schedule.every().thursday.at("18:30").do(remind_me, message="Gym Session in 1 hour")

def print_today_schedule():
    today = datetime.today().strftime('%A')
    print(f"Today's Schedule ({today}):")
    logging.info(f"Today's Schedule ({today}):")

def main():
    set_daily_standup()
    set_monday_wednesday_sessions()
    set_friday_project_review()
    set_gym_sessions()

    schedule.every().day.at("09:37").do(print_today_schedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

main()