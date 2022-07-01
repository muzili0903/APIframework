# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/24 17:42
@file    :scheduler.py
"""
from apscheduler.schedulers.blocking import BlockingScheduler
from com.core.APIrun import run


def scheduler_params(con):
    """
    :param con:
    :return:
    """
    params = "scheduler.add_job(run, 'interval'"
    weeks = con.get_config_int('scheduler', 'weeks')
    days = con.get_config_int('scheduler', 'days')
    hours = con.get_config_int('scheduler', 'hours')
    minutes = con.get_config_int('scheduler', 'minutes')
    seconds = con.get_config_int('scheduler', 'seconds')
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


def scheduler_py(con):
    """
    :param con:
    :return:
    """
    scheduler = BlockingScheduler()
    eval(scheduler_params(con))
    scheduler.start()


if __name__ == "__main__":
    pass
