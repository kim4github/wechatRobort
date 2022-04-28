import pyperclip
from apscheduler.schedulers.blocking import BlockingScheduler

import CHAT
import ImageSender


def APschedulerMonitor():
  # 创建调度器：BlockingScheduler
  scheduler = BlockingScheduler()
  scheduler.add_job(Task, 'cron', hour='9-20', id='test_job1')
  scheduler.add_job(Task2, 'cron', hour='10,13,19', id='test_job2')

  scheduler.start()

import datetime
def Task():
  now = datetime.datetime.now()
  ts = now.strftime('%Y-%m-%d %H:%M:%S')
  print("定时播报")
  print(ts)
  CHAT.sendTextMessage("小团团 播报")
  ImageSender.sendMessage("小团团 播报")

def Task2():
  now = datetime.datetime.now()
  ts = now.strftime('%Y-%m-%d %H:%M:%S')
  print("定时播报")
  print(ts)

  CHAT.sendTextMessage("小团团 早上好")
  ImageSender.sendMessage("小团团 今日疫情")
