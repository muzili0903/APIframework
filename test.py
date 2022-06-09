# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/1 16:56
@file    :test.py
"""
import pytest


def test_1():
    assert 1 == 2


if __name__ == "__main__":
    pytest.main(['-vs', '--reruns', '2'])
    pass
