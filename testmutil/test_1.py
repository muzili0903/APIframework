# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/1 16:56
@file    :test_1.py
"""
import pytest


@pytest.mark.parametrize('a', [1, 2, 3])
def test_1(a):
    print(a)


if __name__ == "__main__":
    pass
