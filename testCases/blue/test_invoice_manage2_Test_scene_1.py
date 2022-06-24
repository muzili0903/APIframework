#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: muzili
import logging
import allure
import pytest

from com.core.checkResult import check_res
from com.core.initializeParam import ini_package
from com.core import reqSends
from com.core import reqSend

test_case = [{'blue': {'step_1': {'script': {'request_header': {'base_url': 'https://fenqitest.midea.com', 'env': '/invoice_sit', 'Method': 'post', 'path': '/invoice/trans/blue', 'Connection': 'keep-alive', 'timeout': 10, 'sleep_time': 0, 'is_login': False}, 'request_body': {'appId': '${appId}', 'appKey': '${appKey}', 'data': {'invoiceAmt': 610.0, 'immediateInvoice': 1, 'payTaxpayerName': '${payTaxpayerName}', 'invoiceHead': 1, 'bizId': 'biz$(fdate)$(ftime)', 'invoiceType': 3, 'remarks': '票面备注：客户名称：${payTaxpayerName}, bizId=biz$(fdate)$(ftime)$(fnum::2)', 'taxpayerCode': '${taxpayerCode}', 'businessNo': '$(fdate)$(ftime)$(fnum::4)', 'detailList': [{'standards': 'MT-TZBKC01', 'taxRate': 0.13, 'taxUnitPrice': 180.0, 'businessNo': '$(fdate)$(ftime)$(fnum::2)', 'goodCount': 1, 'goodUnit': '台', 'bizDetailId': 'bdid$(fnum::11)', 'amtContainTax': 180.0, 'taxCode': '1080422', 'goodsName': 'Micca 炊具'}, {'standards': 'MP-SJ20W101', 'taxRate': 0.13, 'taxUnitPrice': 430.0, 'businessNo': '$(fdate)$(ftime)$(fnum::2)', 'goodCount': 1, 'goodUnit': '台', 'bizDetailId': 'bdid$(fnum::11)', 'amtContainTax': 430.0, 'taxCode': '107060112', 'goodsName': 'Midea/美的 餐饮具'}]}}, 'check_body': {'check_json': {'check_type': 'perfect_match', 'expected_code': 200, 'expected_result': 'blue_response.json'}, 'check_part': {'check_type': 'in', 'expected_code': 200, 'expected_result': {'code': '00000'}}}}, 'data': {'appId': 'IBCP', 'appKey': '123456', 'payTaxpayerName': 'muzili_blue', 'taxpayerCode': '440001999999260'}}}}, {'batchConfirm': {'step_2': {'script': {'request_header': {'Method': 'post', 'path': '/mage/manual/batchConfirm', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'timeout': 10, 'sleep_time': 0, 'is_login': True}, 'request_body': {'str': '$DB{id}'}, 'check_body': {'check_json': {'check_type': 'perfect_match', 'expected_code': 200, 'expected_result': 'batchConfirm_response.json'}}}, 'data': {'sql': "['select id from t_invoice_to_confirm where business_no = $Req{blue.data.businessNo}']"}}}}, {'batchInvoice': {'step_3': {'script': {'request_header': {'Method': 'post', 'path': '/mage/draft/batchInvoice', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'timeout': 10, 'sleep_time': 0, 'is_login': True}, 'request_body': {'str': '$DB{id}'}, 'check_body': {'check_json': {'check_type': 'perfect_match', 'expected_code': 200, 'expected_result': 'batchInvoice_response.json'}}}, 'data': {'sql': "['select id from t_invoice_trans where business_no = $Req{blue.data.businessNo}']"}}}}]


@pytest.mark.parametrize("test_case", test_case)
@allure.story("test_test_scene_1")
def test_test_scene_1(login_manage, test_case):
    api_name = list(test_case.keys())[0]
    api_content = list(test_case.values())[0]
    api_step = list(api_content.keys())[0]
    api_step_content = list(api_content.values())[0]
    test_info = api_step_content['script']
    test_data = api_step_content['data']
    expect_data = test_info.get('check_body')
    api_info = ini_package(test_info, test_data)
    if api_info.get('is_login'):
        request = login_manage
        result = reqSends.requestSend(request, api_step, api_name, api_info)
    else:
        result = reqSend.requestSend(api_step, api_name, api_info)
    assert True == check_res(result, expect_data)
    

if __name__ == '__main__':
    pytest.main(['-v', './test_invoice_manage2_Test_scene_1'])
