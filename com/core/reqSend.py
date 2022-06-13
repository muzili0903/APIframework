"""
@Time ： 2022/5/18 21:58
@Auth ： muzili
@File ： reqSend.py
@IDE  ： PyCharm
"""
import logging
from time import sleep

import allure

from com.core import reqMethod
from com.util.glo import GolStatic


# TODO
def requestSend(api_step, api_name, case: dict):
    """
    发送请求
    :param api_step: 请求步骤
    :param api_name: 接口名称
    :param case:
    :return:
    """
    logging.info("请求地址：>>>{}".format(case.get('url')))
    logging.info("请求方法：>>>{}".format(case.get('method')))
    logging.info("请求头：>>>{}".format(case.get('headers')))
    logging.info("请求体：>>>{}".format(case.get('data')))
    logging.info("请求cookies：>>>{}".format(case.get('cookies')))
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
        res = reqMethod.post(url=case.get('url'), data=case.get('data'), content_type=case.get('content_type'),
                             headers=case.get('headers'), timeout=case.get('timeout'), cookies=case.get('cookies'),
                             save_cookie=case.get('save_cookie'))
        # res = {'response_code': 200, 'response_body': {'code': '00000', 'msg': '操作成功'}}
    elif case.get('method').lower() == 'get':
        res = reqMethod.get(url=case.get('url'), params=case.get('data'), headers=case.get('headers'),
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
    case = {'url': 'https://fenqitest.midea.com/invoice_sit/invoice/trans/blue', 'method': 'POST',
            'data': {
                "appId": "IBCP",
                "appKey": "123456",
                "data": {
                    "invoiceAmt": 610.0,
                    "immediateInvoice": 1,
                    "payTaxpayerName": "muzili",
                    "invoiceHead": 1,
                    "bizId": "DZFP2022052513300771",
                    "invoiceType": 3,
                    "remarks": "票面备注：客户名称：muzili, bizId=DZFP2022052513300771",
                    "taxpayerCode": "440002999999441",
                    "businessNo": "202205251330079",
                    "detailList": [
                        {
                            "standards": "MT-TZBKC01",
                            "taxRate": 0.13,
                            "taxUnitPrice": 180.00,
                            "businessNo": "DZFP202205251330077",
                            "goodCount": 1,
                            "goodUnit": "台",
                            "bizDetailId": "PFMX36613273604",
                            "amtContainTax": 180.00,
                            "taxCode": "1080422",
                            "goodsName": "Micca 炊具"
                        },
                        {
                            "standards": "MP-SJ20W101",
                            "taxRate": 0.13,
                            "taxUnitPrice": 430.00000000,
                            "businessNo": "DZFP202205251330077",
                            "goodCount": 1,
                            "goodUnit": "台",
                            "bizDetailId": "PFMX75766112740",
                            "amtContainTax": 430.00,
                            "taxCode": "107060112",
                            "goodsName": "Midea/美的 餐饮具"
                        }
                    ]
                }
            },
            'headers': {'Content-Type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
                        'Connection': 'keep-alive', 'token': 'None'},
            'timeout': 10,
            'content_type': 'application/json'}
    reponse_body = {'response_code': 200, 'response_body': {'code': '00000', 'msg': '操作成功'}}
    requestSend('test', case)
