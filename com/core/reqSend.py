"""
@Time ： 2022/5/18 21:58
@Auth ： muzili
@File ： reqSend.py
@IDE  ： PyCharm
"""
import logging

from com.core import reqMethod


# TODO
def requestSend(case: dict, **kwargs):
    """
    发送请求
    :param case:
    :param kwargs:
    :return:
    """
    logging.info("请求地址：>>>{}".format(case.get('url')))
    logging.info("请求方法：>>>{}".format(case.get('method')))
    logging.info("请求头：>>>{}".format(case.get('headers')))
    logging.info("请求体：>>>{}".format(case.get('data')))
    if case.get('method').lower() == 'post':
        res = reqMethod.post(url=case.get('url'), data=case.get('data'), content_type=case.get('content_type'),
                             headers=case.get('headers'), timeout=case.get('timeout'))
    elif case.get('method').lower() == 'get':
        res = reqMethod.get(url=case.get('url'), params=case.get('data'), headers=case.get('headers'),
                            timeout=case.get('timeout'))


if __name__ == "__main__":
    case = {'url': 'http://www.baidu.com/invoice_sit/api/register/getAdultCurbactList', 'method': 'GET',
            'data': {'summary': 'getAdultCurbactList', 'test': 'get_test'},
            'headers': {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
                        'Connection': 'keep-alive', 'token': 'None'}, 'timeout': 10,
            'content_type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    requestSend(case)
