# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/1 16:56
@file    :test.py
"""
import logging
import re

import requests


res = requests.get(url='http://www.baidu.com')
print(res.cookies)


if __name__ == "__main__":

    print('' is None)
    pass
