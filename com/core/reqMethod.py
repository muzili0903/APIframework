"""
@Time ： 2022/5/18 19:39
@Auth ： muzili
@File ： reqMethod.py
@IDE  ： PyCharm
"""
import requests
import logging
import json
import urllib3

from com.util.getConfig import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def post(url, data, content_type, headers=None, timeout=30, cookies=None, save_cookie=False):
    """
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
        data = json.dumps(data)
        response = requests.post(url=url,
                                 json=data,
                                 headers=headers,
                                 timeout=timeout,
                                 cookies=cookies,
                                 verify=False)
    # application/x-www-form-urlencoded
    elif 'x-www-form-urlencoded' in content_type:
        response = requests.post(url=url,
                                 data=data,
                                 headers=headers,
                                 timeout=timeout,
                                 cookies=cookies,
                                 verify=False)
    # multipart/form-data
    elif 'form-data' in content_type:
        with open(data.get('file'), 'rb', encoding='utf8') as fs:
            content = fs.read()
        files = {'file': content}
        response = requests.post(url=url,
                                 files=files,
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
            if save_cookie:
                con = Config()
                con.set_config(section='request_headers', option='cookie', value=response.cookies.get_dict())
            return {'response_code': response.status_code, 'response_body': response.json()}
    except Exception as e:
        logging.error("post请求异常: >>>{}".format(e))
        return None


def get(url, params, headers=None, timeout=30, cookies=None, save_cookie=False):
    """
    :param url: 请求地址
    :param params: 请求参数
    :param headers: 请求头
    :param timeout:
    :param cookies:
    :param save_cookie:
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
        if save_cookie:
            con = Config()
            con.set_config(section='request_headers', option='cookie', value=response.cookies.get_dict())
        return {'response_code': response.status_code, 'response_body': response.json()}
    except Exception as e:
        logging.error("get请求异常: >>>{}".format(e))
        return None


if __name__ == "__main__":
    pass
