# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/20 23:31
@Auth ： muzili
@File ： sysFunc.py.py
@IDE  ： PyCharm
"""
import logging
import random

def unum(length=1):
    """
    生成随机整数
    :return:
    """
    try:
        length = int(length)
    except ValueError:
        logging.error("fnum传参有误，请传int类型>>>{}".format(length))
    nums = ''
    for i in range(length):
        nums = nums + str(random.randint(0, 9))
    return nums


if __name__ == "__main__":
    pass
