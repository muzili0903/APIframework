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
    'request_header': {'path': '/api/register/getAdultCurbactList', 'connection': 'keep-alive',
                       'timeout': 10},
    'request_body': {'appId': '$(fnum::length=6)', 'appKey': '$(unum::2)', 'token': '${token}'}, 'check_body': {
        'check_1': {'check_type': 'check_json', 'expected_code': 200,
                    'expected_result': 'getAdultCurbactList_response.json'}, 'check_2': {'check_type': 'check_db'}}},
                                  'data': {'appKey': 'test1', 'token': '123'}}}}]


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
    # result = requestSend(api_info)
    # check_res(result, expect_data)
    pass


if __name__ == "__main__":
    pass
