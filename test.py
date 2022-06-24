# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/23 9:12
@file    :test.py
"""
import multiprocessing
import os
from multiprocessing import Lock

import pytest

from com.util.glo import GolStatic

if __name__ == "__main__":
    args_list = [['-vs', './testmutil/test1'], ['-vs', './testmutil/test2']]
    lock = Lock()
    for args in args_list:
        process = multiprocessing.Process(target=pytest.main, args=(args,))
        process.start()
    print(GolStatic.get_case_temp(filename='test_1'))
