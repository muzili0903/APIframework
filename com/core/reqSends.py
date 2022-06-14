# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/14 12:04
@file    :reqSends.py
"""
import logging
from time import sleep

import allure

from com.core import reqMethods
from com.util.glo import GolStatic


# TODO
def requestSend(request, api_step, api_name, case: dict):
    """
    发送请求
    :param request:
    :param api_step: 请求步骤
    :param api_name: 接口名称
    :param case:
    :return:
    """
    logging.info("请求地址：>>>{}".format(case.get('url')))
    logging.info("请求方法：>>>{}".format(case.get('method')))
    logging.info("请求头：>>>{}".format(case.get('headers')))
    logging.info("请求体：>>>{}".format(case.get('data')))
    logging.info("请求cookies：>>>{}".format(request.cookies))
    with allure.step("请求步骤: {api_step}, 接口名: {api_name}".format(api_step=api_step, api_name=api_name)):
        allure.attach(name="请求方法", body=str(case.get('method')))
        allure.attach(name="请求地址", body=str(case.get('url')))
        allure.attach(name="请求头", body=str(case.get('headers')))
        allure.attach(name="请求参数", body=str(case.get('data')))
    res = None
    # 存下接口的请求报文
    GolStatic.set_file_temp(filename=api_name, key='request_body', value=case.get('data'))
    if case.get('method').lower() == 'post':
        # 测试临时挡板
        res = reqMethods.post(request, url=case.get('url'), data=case.get('data'),
                              content_type=case.get('content_type'),
                              headers=case.get('headers'), timeout=case.get('timeout'), cookies=case.get('cookies'),
                              save_cookie=case.get('save_cookie'))
        # res = {'response_code': 200, 'response_body': {'code': '00000', 'msg': '操作成功'}}
    elif case.get('method').lower() == 'get':
        res = reqMethods.get(request, url=case.get('url'), params=case.get('data'), headers=case.get('headers'),
                             timeout=case.get('timeout'), cookies=case.get('cookies'),
                             save_cookie=case.get('save_cookie'))
    # 存下接口的响应报文
    if res is not None:
        GolStatic.set_file_temp(filename=api_name, key='response_body', value=res.get('response_body'))
    else:
        GolStatic.set_file_temp(filename=api_name, key='response_body', value=res)
    # 强制等待
    sleep(case.get('sleep_time'))
    return res


if __name__ == "__main__":
    pass
