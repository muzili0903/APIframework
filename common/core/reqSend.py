# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/27 18:03
@file    :reqSend.py
"""
import allure

from common.core import reqMethod
from common.core.initializeParam import ini_package
from common.util.globalVars import GolStatic
from common.util.logOperation import logger


def requestSend(request, api_step: str = None, api_name: str = None, case: dict = None,
                request_body: dict = None) -> dict:
    """
    发送请求
    :param request:
    :param api_step: 请求步骤
    :param api_name: 接口名称
    :param case: 用例
    :param request_body: 用例参数化
    :return:
    """
    case_body = ini_package(case_body=case.get('data'), body_value=request_body)
    logger.info("请求地址：>>>{}".format(case.get('url')))
    logger.info("请求方法：>>>{}".format(case.get('method')))
    logger.info("请求头：>>>{}".format(case.get('headers')))
    logger.info("请求体：>>>{}".format(case_body))
    with allure.step("请求步骤: {api_step}, 接口名: {api_name}".format(api_step=api_step, api_name=api_name)):
        allure.attach(name="请求地址", body=str(case.get('url')))
        allure.attach(name="请求方法", body=str(case.get('method')))
        allure.attach(name="请求头", body=str(case.get('headers')))
        allure.attach(name="请求参数", body=str(case.get('data')))
    # 存下接口的请求报文
    GolStatic.set_file_var(filename=api_name, key='request_body', value=case.get('data'))
    if case.get('method').lower() == 'post':
        res = reqMethod.post(request, url=case.get('url'), data=case.get('data'),
                             content_type=case.get('content_type'),
                             headers=case.get('headers'), timeout=case.get('timeout'))
    elif case.get('method').lower() == 'get':
        res = reqMethod.get(request, url=case.get('url'), params=case.get('data'), headers=case.get('headers'),
                            timeout=case.get('timeout'))
    else:
        logger.error("请求方法不存在: >>>{}".format(case.get('method')))
        raise "请求方法不存在"
    # 存下接口的响应报文
    if res is not None:
        GolStatic.set_file_var(filename=api_name, key='response_body', value=res.get('response_body'))
    else:
        GolStatic.set_file_var(filename=api_name, key='response_body', value=res)
    return res


if __name__ == '__main__':
    ...
