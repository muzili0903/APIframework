# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/28 17:32
@file    :initializeParam.py
"""
import re

from common.core import replaceData
from common.util.globalVars import GolStatic
from common.util.logOperation import logger


def ini_request_headers(request_headers: dict, test_data: dict) -> dict:
    """
    请求头处理
    :param request_headers:
    :param test_data
    :return:
    """
    MYCONFIG = GolStatic.get_pro_var('MYCONFIG')
    try:
        default_headers = dict(MYCONFIG.get_items('HEADERS'))
        default_project = dict(MYCONFIG.get_items('PROJECT'))
    except Exception as e:
        logger.error("配置文件request_headers 或 default_project 不存在: >>>{default_headers}, {default_project}".format(
            default_headers=default_headers, default_project=default_project))
        logger.error("报错信息: >>>{}".format(e))
        raise e
    # headers
    method = request_headers.get('Method') or default_headers.get('Method')
    content_type = request_headers.get('Content-Type') or default_headers.get('Content-Type')
    user_agent = request_headers.get('User-Agent') or default_headers.get('User-Agent')
    connection = request_headers.get('Connection') or default_headers.get('Connection')
    timeout = request_headers.get('timeout') or default_headers.get('timeout')
    base_url = request_headers.get('base_url') or default_project.get('base_url')
    logger.info("request_headers处理前: >>>{}".format(request_headers))
    try:
        header = {'Method': method, 'Content-Type': content_type, 'User-Agent': user_agent, 'Connection': connection,
                  'timeout': int(timeout), 'base_url': base_url}
        header = eval(replaceData.replace_user_var(str(header), test_data))
        request_headers.update(header)
    except Exception as e:
        logger.error("request_headers处理失败: >>>{}".format(e))
    logger.info("request_headers处理后: >>>{}".format(request_headers))
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
    logger.info("body处理前: >>>{}".format(test_info))
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
    logger.info("body处理后: >>>{}".format(test_info))
    return test_info


def ini_package(script: dict, data: dict) -> dict:
    """
    组装报文
    :param script: 脚本文件内容
    :param data: 脚本文件对应的数据
    :return:
    """
    header = ini_request_headers(script.get('request_header'), data)
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
    return {"url": url, "method": method, "data": body, "headers": header_copy, "timeout": timeout,
            "content_type": content_type, "is_login": is_login, "cookies": cookies, "save_cookie": save_cookie,
            'sleep_time': sleep_time}


if __name__ == '__main__':
    ...
