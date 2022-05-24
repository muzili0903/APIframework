# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/19 12:15
@file    :initializeParam.py
"""
import logging
import re

from com.core import replaceData
from com.util.getFileDirs import APISCENE
from com.util.getConfig import Config
from com.util.yamlOperation import read_yaml
from com.util.fileOperation import get_all_file, get_file_name
from com.util.caseOperation import get_scene


def ini_request_headers(request_headers: dict, test_data: dict) -> dict:
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
    path = request_headers.get('path') or con.get('path')
    logging.info("request_headers处理前>>>{}".format(request_headers))
    try:
        header = {'Method': method, 'Content-Type': content_type, 'User-Agent': user_agent, 'Connection': connection,
                  'timeout': int(timeout), 'token': token, 'path': path}
        header = eval(replaceData.replace_user_var(str(header), test_data))
        request_headers.update(header)
    except Exception as e:
        logging.error("request_headers处理失败>>>{}".format(e))
    logging.info("request_headers处理后>>>{}".format(request_headers))
    return request_headers


def ini_params(test_info: dict, test_data: dict) -> dict:
    """
    初始化报文
    :param test_info：测试报文
    :param test_data: 测试数据
    :return:
    """
    logging.info("body处理前>>>{}".format(test_info))
    # 用户自定义参数化
    if re.search('\$\{.*?\}', str(test_info)) is not None:
        test_info = eval(replaceData.replace_user_var(str(test_info), test_data))
    # 系统函数参数化
    if re.search('\$\(f.*?\)', str(test_info)) is not None:
        test_info = eval(replaceData.replace_func(str(test_info)))
    # 用户自定义函数参数化
    if re.search('\$\(u.*?\)', str(test_info)) is not None:
        test_info = eval(replaceData.replace_user_func(str(test_info)))
    logging.info("body处理后>>>{}".format(test_info))
    # 从请求报文获取参数值
    if False:
        replaceData.replace_req()
    # 从响应报文获取参数值
    if False:
        replaceData.replace_resp()
    # 从数据库获取参数值
    if False:
        replaceData.replace_db()
    return test_info


def ini_package(script, data):
    # 组装报文
    print(script)
    print(data)
    pass


if __name__ == "__main__":
    headers = {"Method": "GET", "User-Agent": "${name}", "appId": "$(fnum::length=6)",
               "appKey": "$(unum::2)"}
    # # ini_request_headers(headers, {"name": "muzili"})
    # # print(headers)
    # from com.util.getFileDirs import APIYAML, APIDATA
    #
    # file = APIYAML + '\\test.yaml'
    # case = read_yaml(file)
    # file = APIDATA + '\\test.ini'
    # c = Config(file)
    # # print(case)
    # data = dict(c.get_items('test'))
    # # print("data:", data)
    # case = ini_request_headers(eval(case), data)
    # print(case)
    # test_info = ini_params(headers, {"name": "muzili"})
    # print(test_info)
    test = {
        'script': {
            'request_header': {
                'method': '${method}'
            },
            'request_body': {
                'summary': 'getAdultCurbactList',
                'test': 'get_test'
            }
        },
        'data': {
            'appKey': 'test2',
            'AppKey11': 'Test211'
        }
    }
    ini_package(test.get('script'), test.get('data'))
    pass
