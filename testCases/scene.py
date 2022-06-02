# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/31 8:26
@file    :scene.py
"""
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
        'check_json': {'check_type': 'perfect_match', 'expected_code': 200, 'expected_result': 'test_response.json'}}},
    'data': {'appId': 'IBCP', 'appKey': '123456'}}}}]


# test_step = list()
# for case in test_case:
#     for key, value in case.items():
#         test_step.append(key)
# print(test_step)
#

@pytest.mark.parametrize("test_case", test_case)
# @allure.story("test_findParam")
def test_findParam(test_case):
    # api_name = list(test_case.keys())[0]
    api_content = list(test_case.values())[0]
    # api_step = list(api_content.keys())[0]
    api_step_content = list(api_content.values())[0]
    test_info = api_step_content['script']
    test_data = api_step_content['data']
    expect_data = test_info.pop('check_body')
    api_info = ini_package(test_info, test_data)
    print('test_info:', test_info)
    print('test_data:', test_data)
    print('expect_data:', expect_data)
    print('api_info:', api_info)
    result = requestSend(api_info)
    print('result:', result)
    # print(check_res(result, expect_data))
    assert True == check_res(result, expect_data)
    pass


if __name__ == "__main__":
    pytest.main(['-v', './scene.py'])
    pass
