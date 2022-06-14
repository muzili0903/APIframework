# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/1 16:56
@file    :test.py
"""
import logging
import re
from time import sleep
import requests

request_header = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded'
}

url1 = r'https://efssit.midea.com/admin/'

# request = requests.session()

res1 = requests.get(url=url1, headers=request_header, verify=False)
# print(res1.status_code)
# print(res1.json())


test = {
    'url': 'https://signinuat.midea.com/login?service=https://efssit.midea.com/admin/',
    'header': {'Content-Type': 'application/x-www-form-urlencoded'},
    'data': {'username': 'libl6',
             'password': '2uQptrz/K7yEpld+sRp3vQ==',
             'execution': 'e1s1',
             '_eventId': 'submit',
             'geolocation': ''}
}

# test.get('data').update({'Cookie': res1.cookies.get_dict()})
cookies = requests.utils.cookiejar_from_dict(res1.cookies)
res = requests.post(url=test.get('url'), headers=test.get('header'), data=test.get('data'),
                    cookies=cookies)
print(res.cookies.get_dict())
print(res.status_code)
# print(res.json())

test1 = {
    'url': r'https://efssit.midea.com/ecr-admin/invoice_api/mage/manual/addInvoiceToConfirm',
    'header': {'Connection': 'keep-alive', 'Content-Type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'},
    'data': {'appId': 'IBCP', 'appKey': '123456',
             'data': {'id': '', 'invoiceType': '1',
                      'invoiceHead': '1',
                      'erpCustCode': '', 'sysSource': '0',
                      'autoSendFlag': '0', 'ouName': '',
                      'ouCode': '',
                      'payTaxpayerName': 'muzili',
                      'payTaxpayerCode': '',
                      'payUnitAddress': '220610',
                      'payFixedPhoneNumber': '220610',
                      'businessNos': 'DZFP202206131631520162',
                      'mail': '220610',
                      'messagePhone': '220610',
                      'payBankName': '220610',
                      'payBankAccount': '220610',
                      'invoiceToConfirmDetailBOList': [{
                          'businessNo': 'DZFP2022061316315212',
                          'goodsName': '石狮子',
                          'goodsId': 204,
                          'goodsCode': '17122000041283',
                          'standards': '220610',
                          'goodsUnit': '只',
                          'goodsCount': 1,
                          'taxUnitPrice': 100,
                          'notTaxUnitPrice': 88.5,
                          'amtContainTax': 100,
                          'amtNotContainTax': 88.5,
                          'taxAmt': 11.5,
                          'taxClassificationId': 999,
                          'taxName': '矿产品',
                          'taxFullName': '其他矿产品',
                          'taxRate': 0.13,
                          'taxCode': '1020600000000000000',
                          'shortTaxCode': '10206'},
                          {
                              'businessNo': 'DZFP2022061316315249',
                              'goodsName': '收音机',
                              'goodsId': 179,
                              'goodsCode': '963852741',
                              'standards': '220610',
                              'goodsUnit': '件',
                              'goodsCount': 2,
                              'taxUnitPrice': 100,
                              'notTaxUnitPrice': 88.495,
                              'amtContainTax': 200,
                              'amtNotContainTax': 176.99,
                              'taxAmt': 23.01,
                              'taxClassificationId': 999,
                              'taxName': '绘图测量仪器',
                              'taxFullName': '数学计算器具',
                              'taxRate': 0.13,
                              'taxCode': '1090604040000000000',
                              'shortTaxCode': '109060404'}],
                      'recTaxpayerId': 269,
                      'recTaxpayerName': '百鸣鸟装饰有限公司',
                      'recTaxpayerCode': '440001999999260',
                      'reviewer': '沙和尚', 'receiver': '猪八戒',
                      'openMan': '孙悟空',
                      'remarks': '220610',
                      'recUnitAddress': '佛山市顺德区北滘美的大道148号',
                      'recFixedPhoneNumber': '0817-25945214',
                      'recBankName': '中国农商银行佛山北滘支行',
                      'recBankAccount': '1845822362245224477',
                      'invoiceByHandFlag': 1, 'amount': '',
                      'deviceId': 234, 'deviceType': 1,
                      'amtNotContainTax': 265.49,
                      'taxAmt': 34.51, 'invoiceAmt': 300,
                      'blueInvoiceNo': '',
                      'blueInvoiceCode': '',
                      'redRushInfoNo': ''}}
}
cookies = requests.utils.cookiejar_from_dict(res.cookies)
res2 = requests.post(url=test1.get('url'), headers=test1.get('header'), data=test1.get('data'),
                     cookies=cookies)

print(res.cookies.get_dict())
print(res2.cookies.get_dict())
print(res2.status_code)
print(res2.json())

if __name__ == "__main__":
    pass
