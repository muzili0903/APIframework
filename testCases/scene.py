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
    'request_header': {'method': '${method}', 'path': '/api/register/getAdultCurbactList', 'connection': 'keep-alive',
                       'timeout': 10},
    'request_body': {'summary': 'getAdultCurbactList', 'describe': 'test_getAdultCurbactList', 'parameter': {
        'params': {'unitCode': '3202112002', 'first': 0, 'pym': '', 'pageSize': 10, 'page': 0}}, 'check_body': {
        'check_1': {'check_type': 'check_json', 'expected_code': 200,
                    'expected_result': 'getAdultCurbactList_response.json'}, 'check_2': {'check_type': 'check_db'}}}},
                                  'data': {'appKey': 'test1'}}}}, {'test2': {'step_2': {
    'script': {'request_header': {'method': '${method}'},
               'request_body': {'summary': 'getAdultCurbactList', 'test': 'get_test'}},
    'data': {'appKey': 'test2', 'AppKey11': 'Test211'}}}}]


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
    api_info = ini_package(test_info, test_data)
    result = requestSend(api_info)
    check_res(result, test_case['data'])
    pass


if __name__ == "__main__":
    pass
