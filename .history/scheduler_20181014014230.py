import schedule
import time
import midtermelections


def run():
    midtermelections.parse_subreddits()


schedule.every().day.at("01:00").do(run, 'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute
