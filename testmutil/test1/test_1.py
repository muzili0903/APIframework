# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/1 16:56
@file    :test_1.py
"""
import os
import time

import pytest
from com.util.glo import GolStatic

GolStatic.set_case_temp(filename='test_1', value=[1, 2, 3])


@pytest.mark.parametrize('a', GolStatic.get_case_temp(filename='test_1'))
def test_1(a):
    print(os.getpid())
    print('test_1中的a', a)
    time.sleep(20)
    GolStatic.set_case_temp(filename='test_1', value=123)
    print('test_1中的test_1', GolStatic.get_case_temp(filename='test_1'))

@pytest.mark.parametrize('a', GolStatic.get_case_temp(filename='test_1'))
def test_2(a):
    print(os.getpid())
    time.sleep(25)
    print('test_1中test_2的a', a)


if __name__ == "__main__":
    GolStatic.get_case_temp(filename='test_1')
