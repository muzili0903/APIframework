# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/19 12:15
@file    :initializeParam.py
"""
import logging

from com.util.getConfig import Config
from com.util.yamlOperation import read_yaml
from com.util.fileOperation import get_all_file, get_file_name


def ini_params(test_info, test_data):
    """
    初始化报文
    :param test_info：测试报文
    :param test_data: 测试数据
    :return:
    """
    pass


def ini_package():
    # 组装报文
    pass


if __name__ == "__main__":
    file = r"E:\project\APIframework\api\yaml"
    p = get_all_file(file)
    print(p)
    print(get_file_name(p[0]))
    # case = ini_params(file)
    # print(case)
