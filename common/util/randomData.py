# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/25 15:05
@file    :randomData.py
"""
import random
import time
from datetime import datetime


def get_current_time() -> str:
    """
    yyyymmddHHMMSS
    :return:
    """
    format_str = '%Y%m%d%H%M%S'
    return datetime.now().strftime(format_str)


def fDATE() -> str:
    """
    返回 yyyy-mm-dd
    :return:
    """
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def fdate() -> str:
    """
    返回 yyyymmdd
    :return:
    """
    return time.strftime('%Y%m%d', time.localtime(time.time()))


def fTIME() -> str:
    """
    返回 HH:MM:SS
    :return:
    """
    return time.strftime('%H:%M:%S', time.localtime(time.time()))


def ftime() -> str:
    """
    返回 HHMMSS
    :return:
    """
    return time.strftime('%H%M%S', time.localtime(time.time()))


def fnum(length: int = 1) -> str:
    """
    生成随机整数
    :return:
    """
    nums = ''
    for i in range(int(length)):
        nums += str(random.randint(0, 9))
    return nums


if __name__ == '__main__':
    ...
