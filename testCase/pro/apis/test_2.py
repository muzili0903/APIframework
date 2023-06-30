# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/28 12:54
@file    :test_2.py
"""
from common.util.yamlOperation import read_folder_case


class TestExample:
    # 通过读excel方式获取接口内容
    test_case = read_folder_case(r"E:\APIAutoTestModel\testData\pro\model")

    def test_1(self, login_and_logout):
        assert 'riskManageList' in self.test_case.keys()

    def test_2(self, login_and_logout):
        assert 1 == 1

    def test_3(self, login_and_logout):
        assert 1 == 1


if __name__ == '__main__':
    pass
