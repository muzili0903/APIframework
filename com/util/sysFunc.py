"""
@Time ： 2022/5/19 19:46
@Auth ： muzili
@File ： sysFunc.py
@IDE  ： PyCharm
"""
import random
import time
import logging


def fDATE():
    """
    返回 yyyy-mm-dd
    :return:
    """
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def fdate():
    """
    返回 yyyymmdd
    :return:
    """
    return time.strftime('%Y%m%d', time.localtime(time.time()))


def fTIME():
    """
    返回 HH:MM:SS
    :return:
    """
    return time.strftime('%H:%M:%S', time.localtime(time.time()))


def ftime():
    """
    返回 HHMMSS
    :return:
    """
    return time.strftime('%H%M%S', time.localtime(time.time()))


def fnum(length=1):
    """
    生成随机整数
    :return:
    """
    try:
        length = int(length)
    except ValueError:
        logging.error("fnum传参有误, 请传int类型: >>>{}".format(length))
    nums = ''
    for i in range(length):
        nums = nums + str(random.randint(0, 9))
    return nums


if __name__ == "__main__":
    pass
