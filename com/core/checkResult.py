# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/26 8:30
@file    :checkResult.py
"""
from com.core import checkData


def check_res(response_body: dict, expect_body: dict):
    """
    校验结果
    :param response_body: 实际结果
    :param expect_body: 预期结果
    :return:
    """
    result = list()
    for key, value in expect_body.items():
        if key.lower() == 'check_json':
            result.append(checkData.check_resp(response_body, value))
        elif key.lower() == 'check_db':
            result.append(checkData.check_db(response_body, value))
        elif key.lower() == 'check_part':
            pass
        elif key.lower() == '':
            pass
        else:
            pass
    if False not in result:
        return True
    else:
        return False


if __name__ == "__main__":
    expect_body = {
        'check_1': {
            'check_type': 'check_json',
            'expected_code': '200',
            'expected_result': 'getAdultCurbactList_response.json'},
        'check_2': {'check_type': 'check_db'}}
    reponse_body = {'response_code': 200, 'response_body': {'code': '00000', 'msg': '操作成功'}}
    print(check_res(reponse_body, expect_body))
    pass
