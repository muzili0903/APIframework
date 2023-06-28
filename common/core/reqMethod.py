# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/27 17:40
@file    :reqMethod.py
"""
from typing import Any

import urllib3

from common.util.logOperation import logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def post(request, url: str, data: dict, content_type: str, headers: dict = None, timeout: int = 30) -> dict:
    """
    :param request:
    :param url: 请求地址
    :param data: 请求参数
    :param content_type: 请求参数格式
    :param headers: 请求头
    :param timeout:
    :return:
    """
    # application/json
    if 'json' in content_type:
        response = request.post(url=url,
                                json=data,
                                headers=headers,
                                timeout=timeout,
                                verify=False)
    # application/x-www-form-urlencoded
    elif 'x-www-form-urlencoded' in content_type:
        response = request.post(url=url,
                                data=data,
                                headers=headers,
                                timeout=timeout,
                                verify=False)
    # multipart/form-data
    elif 'form-data' in content_type:
        with open(data.get('file'), 'rb', encoding='utf8') as fs:
            content = fs.read()
        files = {'file': content}
        response = request.post(url=url,
                                files=files,
                                headers=headers,
                                timeout=timeout,
                                verify=False)
    else:
        response = request.post(url=url,
                                data=data,
                                headers=headers,
                                timeout=timeout,
                                verify=False)
    try:
        if response.status_code != 200:
            return {'response_code': response.status_code, 'response_body': response.text}
        else:
            return {'response_code': response.status_code, 'response_body': response.json()}
    except Exception as e:
        logger.error("post请求异常: >>>{}".format(e))
        raise e


def get(request, url: str, params: Any, headers: dict = None, timeout: int = 30) -> dict:
    """
    :param request:
    :param url: 请求地址
    :param params: 请求参数
    :param headers: 请求头
    :param timeout:
    :return:
    """
    response = request.get(url=url,
                           params=params,
                           headers=headers,
                           timeout=timeout)
    if response.status_code == 301:
        response = request.get(url=response.headers['location'], verify=False)
    try:
        return {'response_code': response.status_code, 'response_body': response.json()}
    except Exception as e:
        logger.error("get请求异常: >>>{}".format(e))
        raise e


if __name__ == "__main__":
    pass
