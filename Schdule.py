import schedule

from datetime import datetime, timedelta, time

def school():
    print("boo")

    # This is for the amount of hours I go to school for
schedule.every(1).hours.until(timedelta(hours=6)).do(school)

def bedtime():
    print('sleeptime')

    schedule.every().day.at("00:00").do(bedtime)

def readBooks():
    print('read a book')

    schedule.every().day.at("22:00").do(readBooks)

def learnLanguages():
    print('Learn about either amaharic or Spainish')

    schedule.every(2).days.do(learnLanguages)

def Gym():
    print('go to gym and workout')

    schedule.every(2).days.do(Gym)

    while True:
    schedule.run_pending()
    time.sleep(1)
