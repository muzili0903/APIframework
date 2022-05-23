# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/19 12:15
@file    :initializeParam.py
"""
import logging

from com.util.getFileDirs import APISCENE
from com.util.getConfig import Config
from com.util.yamlOperation import read_yaml
from com.util.fileOperation import get_all_file, get_file_name
from com.util.caseOperation import get_scene


def ini_request_headers(request_headers: dict, test_data: dict):
    """
    请求头处理
    :param request_headers:
    :param test_data
    :return:
    """
    con = dict(Config().get_items('request_headers'))
    method = request_headers.get('Method') or con.get('Method')
    content_type = request_headers.get('Content-Type') or con.get('Content-Type')
    user_agent = request_headers.get('User-Agent') or con.get('User-Agent')
    connection = request_headers.get('Connection') or con.get('Connection')
    timeout = request_headers.get('timeout') or con.get('timeout')
    token = request_headers.get('token') or con.get('token')
    print(method)
    print(content_type)
    print(user_agent)
    print(connection)
    print(timeout)
    print(token)
    pass


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
    ini_request_headers({"Method": "GET", "User-Agent": "Mozilla"}, {"name": "muzili"})
    # case = ini_params(file)
    # print(case)
    pass
