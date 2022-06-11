#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: muzili
import logging
import allure
import pytest

from com.core.checkResult import check_res
from com.core.initializeParam import ini_package
from com.core.reqSend import requestSend

test_case = [{'addInvoiceToConfirm': {'step_1': {'script': {'request_header': {'method': 'post', 'path': '/mage/manual/addInvoiceToConfirm', 'connection': 'keep-alive', 'timeout': 10, 'save_cookie': True}, 'request_body': {'appId': '${appId}', 'appKey': '${appKey}', 'data': {'id': '', 'invoiceType': '1', 'invoiceHead': '1', 'erpCustCode': '', 'sysSource': '0', 'autoSendFlag': '0', 'ouName': '', 'ouCode': '', 'payTaxpayerName': '${payTaxpayerName}', 'payTaxpayerCode': '', 'payUnitAddress': '220610', 'payFixedPhoneNumber': '220610', 'businessNos': 'DZFP$(fdate)$(ftime)$(fnum::length=4)', 'mail': '220610', 'messagePhone': '220610', 'payBankName': '220610', 'payBankAccount': '220610', 'invoiceToConfirmDetailBOList': [{'businessNo': 'DZFP$(fdate)$(ftime)$(fnum::length=2)', 'goodsName': '石狮子', 'goodsId': 204, 'goodsCode': '17122000041283', 'standards': '220610', 'goodsUnit': '只', 'goodsCount': 1, 'taxUnitPrice': 100, 'notTaxUnitPrice': 88.5, 'amtContainTax': 100, 'amtNotContainTax': 88.5, 'taxAmt': 11.5, 'taxClassificationId': 999, 'taxName': '矿产品', 'taxFullName': '其他矿产品', 'taxRate': 0.13, 'taxCode': '1020600000000000000', 'shortTaxCode': '10206'}, {'businessNo': 'DZFP$(fdate)$(ftime)$(fnum::length=2)', 'goodsName': '收音机', 'goodsId': 179, 'goodsCode': '963852741', 'standards': '220610', 'goodsUnit': '件', 'goodsCount': 2, 'taxUnitPrice': 100, 'notTaxUnitPrice': 88.495, 'amtContainTax': 200, 'amtNotContainTax': 176.99, 'taxAmt': 23.01, 'taxClassificationId': 999, 'taxName': '绘图测量仪器', 'taxFullName': '数学计算器具', 'taxRate': 0.13, 'taxCode': '1090604040000000000', 'shortTaxCode': '109060404'}], 'recTaxpayerId': 269, 'recTaxpayerName': '百鸣鸟装饰有限公司', 'recTaxpayerCode': '440001999999260', 'reviewer': '沙和尚', 'receiver': '猪八戒', 'openMan': '孙悟空', 'remarks': '220610', 'recUnitAddress': '佛山市顺德区北滘美的大道148号', 'recFixedPhoneNumber': '0817-25945214', 'recBankName': '中国农商银行佛山北滘支行', 'recBankAccount': '1845822362245224477', 'invoiceByHandFlag': 1, 'amount': '', 'deviceId': 234, 'deviceType': 1, 'amtNotContainTax': 265.49, 'taxAmt': 34.51, 'invoiceAmt': 300, 'blueInvoiceNo': '', 'blueInvoiceCode': '', 'redRushInfoNo': ''}}, 'check_body': {'check_json': {'check_type': 'perfect_match', 'expected_code': 200, 'expected_result': 'addInvoiceToConfirm_response.json'}}}, 'data': {'appId': 'IBCP', 'appKey': '123456', 'payTaxpayerName': 'muzili'}}}}]


@pytest.mark.parametrize("test_case", test_case)
@allure.story("test_test_scene_1")
def test_test_scene_1(test_case):
    api_name = list(test_case.keys())[0]
    api_content = list(test_case.values())[0]
    api_step = list(api_content.keys())[0]
    api_step_content = list(api_content.values())[0]
    test_info = api_step_content['script']
    test_data = api_step_content['data']
    expect_data = test_info.get('check_body')
    api_info = ini_package(test_info, test_data)
    result = requestSend(api_step, api_name, api_info)
    assert True == check_res(result, expect_data)
    

if __name__ == '__main__':
    pytest.main(['-v', './test_invoice_manage_Test_scene_1'])
