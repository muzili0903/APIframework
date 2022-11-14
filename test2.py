# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/29 21:02
@Auth ： muzili
@File ： test2.py
@IDE  ： PyCharm
"""
import datetime
import re

import requests
import json

import time


def get_fund_info(fund_code):
    """
    获取基金基本信息
    :param fund_code:
    :return:
    # fundcode 基金代码
    # name 基金名称
    # jzrq 净值日期
    # dwjz 当日净值
    # gsz 估算净值
    # gszzl 估算涨跌百分比 即-0.42%
    # gztime 估值时间
    """
    url = r'http://fundgz.1234567.com.cn/js/{fund_code}.js?rt={t}'.format(fund_code=fund_code, t=int(time.time()))
    res = requests.get(url=url)
    content = res.text
    # 正则表达式
    pattern = r'^jsonpgz\((.*)\)'
    # 查找结果
    search = re.findall(pattern, content)[0]
    return json.loads(search)


def buy_fund(fund_code, money):
    """
    :param fund_code:
    :param money:
    :return:
    """
    fund_info = get_fund_info(fund_code)


# with open('./fun.json', 'a+', encoding='utf-8') as f:
#     f.write(str(get_fund_info('008888')) + '\n')

now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
dt=datetime.datetime(2020,1,12,12,50,23)
a = datetime.datetime.strftime(dt,"%W") ###星期一为星期的开始
print(dt)
print(a)

