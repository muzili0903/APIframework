#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: muzili
import logging
import allure
import pytest

from com.core.checkResult import check_res
from com.core.initializeParam import ini_package
from com.core.reqSend import requestSend

test_case = [{'test': {'step_1': {'script': {
    'request_header': {'method': 'post', 'path': '/invoice/trans/blue', 'connection': 'keep-alive', 'timeout': 10},
    'request_body': {'appId': '${appId}', 'appKey': '${appKey}',
                     'data': {'invoiceAmt': 610.0, 'immediateInvoice': 1, 'payTaxpayerName': 'muzili', 'invoiceHead': 1,
                              'bizId': 'DZFP$(fdate)$(ftime)$(fnum::length=4)', 'invoiceType': 3,
                              'remarks': '票面备注：客户名称：muzili, bizId=DZFP2022051811024063',
                              'taxpayerCode': '440002999999441', 'businessNo': '$(fdate)$(ftime)', 'detailList': [
                             {'standards': 'MT-TZBKC01', 'taxRate': 0.13, 'taxUnitPrice': 180.0,
                              'businessNo': 'DZFP$(fdate)$(ftime)$(fnum::length=2)', 'goodCount': 1, 'goodUnit': '台',
                              'bizDetailId': 'PFMX$(fnum::length=11)', 'amtContainTax': 180.0, 'taxCode': '1080422',
                              'goodsName': 'Micca 炊具'},
                             {'standards': 'MP-SJ20W101', 'taxRate': 0.13, 'taxUnitPrice': 430.0,
                              'businessNo': 'DZFP$(fdate)$(ftime)$(fnum::length=2)', 'goodCount': 1, 'goodUnit': '台',
                              'bizDetailId': 'PFMX$(fnum::length=11)', 'amtContainTax': 430.0, 'taxCode': '107060112',
                              'goodsName': 'Midea/美的 餐饮具'}]}}, 'check_body': {
        'check_json': {'check_type': 'perfect_match', 'expected_code': 200, 'expected_result': 'addInvoiceToConfirm_response.json'}}},
    'data': {'appId': 'IBCP', 'appKey': '123456'}}}}, {'test': {'step_2': {'script': {
    'request_header': {'method': 'post', 'path': '/invoice/trans/blue', 'connection': 'keep-alive', 'timeout': 10},
    'request_body': {'appId': '${appId}', 'appKey': '${appKey}',
                     'data': {'invoiceAmt': 610.0, 'immediateInvoice': 1, 'payTaxpayerName': 'muzili', 'invoiceHead': 1,
                              'bizId': 'DZFP$(fdate)$(ftime)$(fnum::length=4)', 'invoiceType': 3,
                              'remarks': '票面备注：客户名称：muzili, bizId=DZFP2022051811024063',
                              'taxpayerCode': '440002999999441', 'businessNo': '$(fdate)$(ftime)', 'detailList': [
                             {'standards': 'MT-TZBKC01', 'taxRate': 0.13, 'taxUnitPrice': 180.0,
                              'businessNo': 'DZFP$(fdate)$(ftime)$(fnum::length=2)', 'goodCount': 1, 'goodUnit': '台',
                              'bizDetailId': 'PFMX$(fnum::length=11)', 'amtContainTax': 180.0, 'taxCode': '1080422',
                              'goodsName': 'Micca 炊具'},
                             {'standards': 'MP-SJ20W101', 'taxRate': 0.13, 'taxUnitPrice': 430.0,
                              'businessNo': 'DZFP$(fdate)$(ftime)$(fnum::length=2)', 'goodCount': 1, 'goodUnit': '台',
                              'bizDetailId': 'PFMX$(fnum::length=11)', 'amtContainTax': 430.0, 'taxCode': '107060112',
                              'goodsName': 'Midea/美的 餐饮具'}]}}, 'check_body': {
        'check_json': {'check_type': 'perfect_match', 'expected_code': 200, 'expected_result': 'addInvoiceToConfirm_response.json'}}},
    'data': {
        'appId': 'IBCP',
        'appKey': '123456'}}}}]


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
    pytest.main(['-v', './test_test_Test_scene_1', '--reruns', '10'])
