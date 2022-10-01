from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler


def periodic_execution():# 任意の関数名
    print("Tick! The time is : %s'" % datetime.now())

def start():
    scheduler = BackgroundScheduler()
     # 5分おきに実行
    scheduler.add_job(periodic_execution, 'interval', seconds=5)
    scheduler.start()