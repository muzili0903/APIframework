# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/24 17:42
@file    :scheduler.py
"""
from apscheduler.schedulers.blocking import BlockingScheduler


def scheduler_params(con):
    """
    :param con:
    :return:
    """
    params = "scheduler.add_job(run, 'interval'"
    weeks = eval(con.get_config('scheduler', 'weeks'))
    days = eval(con.get_config('scheduler', 'days'))
    hours = eval(con.get_config('scheduler', 'hours'))
    minutes = eval(con.get_config('scheduler', 'minutes'))
    seconds = eval(con.get_config('scheduler', 'seconds'))
    start_date = eval(con.get_config('scheduler', 'start_date'))
    end_date = eval(con.get_config('scheduler', 'end_date'))
    if weeks is not None:
        params = params + ', ' + 'weeks=' + str(weeks)
    if days is not None:
        params = params + ', ' + 'days=' + str(days)
    if hours is not None:
        params = params + ', ' + 'hours=' + str(hours)
    if minutes is not None:
        params = params + ', ' + 'minutes=' + str(minutes)
    if seconds is not None:
        params = params + ', ' + 'seconds=' + str(seconds)
    if start_date is not None:
        params = params + ', ' + 'start_date=' + str(start_date)
    if end_date is not None:
        params = end_date + ', ' + 'end_date=' + str(end_date)
    return params + ')'


def job_func():
    scheduler = BlockingScheduler()
    scheduler.add_job(job_func, 'interval', hours=2)
    scheduler.start()


if __name__ == "__main__":
    from com.util.getConfig import Config
    con = Config()
    print(scheduler_params(con))
