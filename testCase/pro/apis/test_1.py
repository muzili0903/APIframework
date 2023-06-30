# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/26 16:37
@file    :test_1.py
"""
from common.util.excelOperation import ReadExcel


class TestExample:
    # 通过读excel方式获取接口内容
    test_case = ReadExcel(filename=r'E:\APIAutoTestModel\testData\pro\APIAutoTestDataModel.xlsx').read_to_dict()

    def test_1(self, login_and_logout):
        assert 'riskManageList' in self.test_case.keys()

    def test_2(self, login_and_logout):
        assert 1 == 1

    def test_3(self, login_and_logout):
        assert 1 == 1


if __name__ == '__main__':
    pass
