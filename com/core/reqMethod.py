"""
@Time ： 2022/5/18 19:39
@Auth ： muzili
@File ： reqMethod.py
@IDE  ： PyCharm
"""
import requests
import logging
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def post(url, data, content_type, headers=None, timeout=30, cookies=None):
    """
    :param url: 请求地址
    :param data: 请求参数
    :param content_type: 请求参数格式
    :param headers: 请求头
    :param timeout:
    :param cookies:
    :return:
    """
    if 'application' in content_type:
        response = requests.post(url=url,
                                 json=data,
                                 headers=headers,
                                 timeout=timeout,
                                 cookies=cookies,
                                 verify=False)
    else:
        response = requests.post(url=url,
                                 data=data,
                                 headers=headers,
                                 timeout=timeout,
                                 cookies=cookies,
                                 verify=False)
    try:
        if response.status_code != 200:
            return {'response_code': response.status_code, 'response_body': response.text}
        else:
            return {'response_code': response.status_code, 'response_body': response.json()}
    except Exception as e:
        logging.error("post请求异常>>>{}".format(e))


def get(url, params, headers=None, timeout=30, cookies=None):
    """
    :param url: 请求地址
    :param params: 请求参数
    :param headers: 请求头
    :param timeout:
    :param cookies:
    :return:
    """
    response = requests.get(url=url,
                            params=params,
                            headers=headers,
                            timeout=timeout,
                            cookies=cookies)
    if response.status_code == 301:
        response = requests.get(url=response.headers['location'], verify=False)
    try:
        return {'response_code': response.status_code, 'response_body': response.json()}
    except Exception as e:
        logging.error("get请求异常>>>{}".format(e))


if __name__ == "__main__":
    pass
