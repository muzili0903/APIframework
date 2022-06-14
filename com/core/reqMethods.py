# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/14 12:07
@file    :reqMethods.py
"""
import logging
import json
import urllib3

from com.util.getConfig import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def post(request, url, data, content_type, headers=None, timeout=30, cookies=None, save_cookie=False):
    """
    :param request:
    :param url: 请求地址
    :param data: 请求参数
    :param content_type: 请求参数格式
    :param headers: 请求头
    :param timeout:
    :param cookies:
    :param save_cookie:
    :return:
    """
    # application/json
    if 'json' in content_type:
        # 多此一举, 发送json数据时,会自动转json格式的数据
        # data = json.dumps(data) body = complexjson.dumps(json, allow_nan=False)
        response = request.post(url=url,
                                json=data,
                                headers=headers,
                                timeout=timeout,
                                # cookies=cookies,
                                verify=False)
    # application/x-www-form-urlencoded
    elif 'x-www-form-urlencoded' in content_type:
        response = request.post(url=url,
                                data=data,
                                headers=headers,
                                timeout=timeout,
                                # cookies=cookies,
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
                                # cookies=cookies,
                                verify=False)
    else:
        response = request.post(url=url,
                                data=data,
                                headers=headers,
                                timeout=timeout,
                                # cookies=cookies,
                                verify=False)
    try:
        if response.status_code != 200:
            return {'response_code': response.status_code, 'response_body': response.text}
        else:
            if save_cookie:
                con = Config()
                con.set_config(section='request_headers', option='cookie', value=str(response.cookies.get_dict()))
            return {'response_code': response.status_code, 'response_body': response.json()}
            # return {'response_code': response.status_code, 'response_body': ''}
    except Exception as e:
        logging.error("post请求异常: >>>{}".format(e))
        return None


def get(request, url, params, headers=None, timeout=30, cookies=None, save_cookie=False):
    """
    :param request:
    :param url: 请求地址
    :param params: 请求参数
    :param headers: 请求头
    :param timeout:
    :param cookies:
    :param save_cookie:
    :return:
    """
    response = request.get(url=url,
                           params=params,
                           headers=headers,
                           timeout=timeout)
    if response.status_code == 301:
        response = request.get(url=response.headers['location'], verify=False)
    try:
        if save_cookie:
            con = Config()
            con.set_config(section='request_headers', option='cookie', value=str(response.cookies.get_dict()))
        return {'response_code': response.status_code, 'response_body': response.json()}
        # return {'response_code': response.status_code, 'response_body': ''}
    except Exception as e:
        logging.error("get请求异常: >>>{}".format(e))
        return None


if __name__ == "__main__":
    pass
