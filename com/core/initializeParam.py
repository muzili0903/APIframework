# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/19 12:15
@file    :initializeParam.py
"""
import logging
import re
from copy import deepcopy

from com.core import replaceData
# from com.util.getFileDirs import APISCENE
from com.util.getConfig import Config


# from com.util.yamlOperation import read_yaml
# from com.util.fileOperation import get_all_file, get_file_name
# from com.util.caseOperation import get_scene


def ini_request_headers(request_headers: dict, test_data: dict, con) -> dict:
    """
    请求头处理
    :param request_headers:
    :param test_data
    :return:
    """
    try:
        default_headers = dict(con.get_items('request_headers'))
        default_project = dict(con.get_items('project'))
    except Exception as e:
        logging.error("配置文件request_headers 或 default_project 不存在: >>>{default_headers}, {default_project}".format(
            default_headers=default_headers, default_project=default_project))
        logging.error("报错信息: >>>{}".format(e))
    # headers
    method = request_headers.get('Method') or default_headers.get('Method')
    content_type = request_headers.get('Content-Type') or default_headers.get('Content-Type')
    user_agent = request_headers.get('User-Agent') or default_headers.get('User-Agent')
    connection = request_headers.get('Connection') or default_headers.get('Connection')
    timeout = request_headers.get('timeout') or default_headers.get('timeout')
    cookie = request_headers.get('cookie') or default_headers.get('cookie')
    save_cookie = request_headers.get('save_cookie') or default_headers.get('save_cookie')
    sleep_time = request_headers.get('sleep_time') or default_headers.get('sleep_time')
    path = request_headers.get('path') or default_headers.get('path')
    # project 兼容上游与管理台之间的交互
    base_url = request_headers.get('base_url') or default_project.get('base_url')
    env = request_headers.get('env') or default_project.get('env')
    logging.info("request_headers处理前: >>>{}".format(request_headers))
    try:
        header = {'Method': method, 'Content-Type': content_type, 'User-Agent': user_agent, 'Connection': connection,
                  'timeout': int(timeout), 'cookie': cookie, 'save_cookie': save_cookie, 'path': path,
                  'base_url': base_url, 'env': env, 'sleep_time': int(sleep_time)}
        header = eval(replaceData.replace_user_var(str(header), test_data))
        request_headers.update(header)
    except Exception as e:
        logging.error("request_headers处理失败: >>>{}".format(e))
    logging.info("request_headers处理后: >>>{}".format(request_headers))
    return request_headers


def ini_db_params(sql: str):
    """
    初始化sql
    :param sql:
    :return:
    """
    # 从请求报文获取参数值
    if re.search('\$Req\{.*?\}', sql) is not None:
        sql = replaceData.replace_req(sql)
    # 从响应报文获取参数值
    if re.search('\$Resp\{.*?\}', sql) is not None:
        sql = replaceData.replace_resp(sql)
    return sql


def ini_params(test_info: dict, test_data: dict) -> dict:
    """
    初始化报文
    :param test_info：测试报文
    :param test_data: 测试数据
    :return:
    """
    logging.info("body处理前: >>>{}".format(test_info))
    # 用户自定义参数化
    if re.search('\$\{.*?\}', str(test_info)) is not None:
        test_info = eval(replaceData.replace_user_var(str(test_info), test_data))
    # 系统函数参数化
    if re.search('\$\(f.*?\)', str(test_info)) is not None:
        test_info = eval(replaceData.replace_func(str(test_info)))
    # 用户自定义函数参数化
    if re.search('\$\(u.*?\)', str(test_info)) is not None:
        test_info = eval(replaceData.replace_user_func(str(test_info)))
    # 从请求报文获取参数值
    if re.search('\$Req\{.*?\}', str(test_info)) is not None:
        test_info = eval(replaceData.replace_req(str(test_info)))
    # 从响应报文获取参数值
    if re.search('\$Resp\{.*?\}', str(test_info)) is not None:
        test_info = eval(replaceData.replace_resp(str(test_info)))
    # 从数据库获取参数值
    if re.search('\$DB\{.*?\}', str(test_info)) is not None:
        test_info = eval(replaceData.replace_db(str(test_info), test_data))
    logging.info("body处理后: >>>{}".format(test_info))
    return test_info


def ini_package(script: dict, data: dict) -> dict:
    """
    组装报文
    :param script: 脚本文件内容
    :param data: 脚本文件对应的数据
    :return:
    """
    con = Config()
    header = ini_request_headers(script.get('request_header'), data, con)
    body = ini_params(script.get('request_body'), data)
    # 深拷贝，失败重跑数据不变
    header_copy = deepcopy(header)
    path = header_copy.pop('path')
    base_url = header_copy.pop('base_url')
    env = header_copy.pop('env')
    timeout = header_copy.pop('timeout')
    method = header_copy.pop('Method')
    cookies = eval(header_copy.pop('cookie'))
    is_login = header_copy.pop('is_login')
    save_cookie = header_copy.pop('save_cookie')
    sleep_time = header_copy.pop('sleep_time')
    content_type = header_copy.get('Content-Type')
    url = base_url + env + path
    # try:
    #     project = dict(con.get_items('project'))
    #     url = project.get('base_url') + project.get('env') + path
    # except Exception as e:
    #     logging.error("配置文件project不存在>>>{}".format(con))
    #     logging.error("报错信息>>>{}".format(e))
    return {"url": url, "method": method, "data": body, "headers": header_copy, "timeout": timeout,
            "content_type": content_type, "is_login": is_login, "cookies": cookies, "save_cookie": save_cookie,
            'sleep_time': sleep_time}


if __name__ == "__main__":
    headers = {"Method": "GET", "User-Agent": "$Resp{name}", "appId": "$(fnum::length=6)",
               "appKey": "$(unum::2)"}
    # # ini_request_headers(headers, {"name": "muzili"})
    # # print(headers)
    # from com.util.getFileDirs import APIYAML, APIDATA
    #
    # file = APIYAML + '\\addInvoiceToConfirm.yaml'
    # case = read_yaml(file)
    # file = APIDATA + '\\invoice_manage.ini'
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
                'path': '/api/register/getAdultCurbactList',
                'Method': '${method}'
            },
            'request_body': {
                'parameter': 'getAdultCurbactList',
                'test': '$DB{process_n1ame}'
            }
        },
        'data': {
            'appKey': 'test2',
            'AppKey11': 'Test211',
            'method': 'GET',
            'sql': '''[
        "select process_name, process_type_id from t_flowable_ent_process_template WHERE process_name = '删除业务类型111' limit 1",
        "select process_name, process_type_id from t_flowable_ent_process_template WHERE process_name = '删除业务类型' limit 1"]'''
        }
    }
    print(ini_package(test.get('script'), test.get('data')))
    pass
