from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from com.util.getConfig import Config


# weeks(int)	间隔几周
# days(int)	间隔几天
# hours(int)	间隔几小时
# minutes(int)	间隔几分钟
# seconds(int)	间隔多少秒
# start_date(datetime or str)	开始日期
# end_date(datetime or str)	结束日期
def scheduler_params(con):
    params = list()
    weeks = eval(con.get_config('scheduler', 'weeks'))
    days = eval(con.get_config('scheduler', 'days'))
    hours = eval(con.get_config('scheduler', 'hours'))
    minutes = eval(con.get_config('scheduler', 'minutes'))
    seconds = eval(con.get_config('scheduler', 'seconds'))
    start_date = eval(con.get_config('scheduler', 'start_date'))
    end_date = eval(con.get_config('scheduler', 'end_date'))
    if weeks is not None:
        params.append('weeks={}'.format(weeks))
    if days is not None:
        params.append('days={}'.format(days))
    if hours is not None:
        params.append('hours={}'.format(hours))
    if minutes is not None:
        params.append('minutes={}'.format(minutes))
    if seconds is not None:
        params.append('seconds={}'.format(seconds))
    if start_date is not None:
        params.append('start_date={}'.format(start_date))
    if end_date is not None:
        params.append('start_date={}'.format(end_date))
    return params


def job_func(param):
    print("当前时间：", datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"))

    scheduler = BlockingScheduler()

    # 每2小时触发
    scheduler.add_job(job_func(param), 'interval', hours=2)

    # 在 2019-04-15 17:00:00 ~ 2019-12-31 24:00:00 之间, 每隔两分钟执行一次 job_func 方法
    scheduler.add_job(job_func(param), 'interval', seconds=2, start_date='2022-06-24', end_date='2022-06-25')

    scheduler.start()


def t(cont=None):
    print(cont)


def tt(l):
    name = ''
    for i in l:
        name = name + i + ', '
    print('interval, ' + name)


l = ['cont=5', 'cont=2']

tt(l)

if __name__ == "__main__":
    con = Config()
    job_func(1)
    print(scheduler_params(con))
