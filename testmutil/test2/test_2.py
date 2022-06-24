# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/23 9:12
@file    :test_2.py
"""
import os
import time

import pytest

from com.util.glo import GolStatic

GolStatic.set_case_temp(filename='test_1', value=[11, 22, 33])


@pytest.mark.parametrize('a', GolStatic.get_case_temp(filename='test_1'))
def test_1(a):
    print(os.getpid())
    print('test_2中的a', a)
    time.sleep(20)
    GolStatic.set_case_temp(filename='test_1', value=112233)
    print('test_2中的test_1', GolStatic.get_case_temp(filename='test_1'))


if __name__ == "__main__":
    print(GolStatic.get_case_temp(filename='test_1'))
