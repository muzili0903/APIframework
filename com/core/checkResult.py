# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/26 8:30
@file    :checkResult.py
"""
import logging

import allure

from com.core import checkData
from com.core.initializeParam import ini_params
from com.util.getFileDirs import APIJSON
from com.util.jsonOperation import read_json


def check_res(response_body: dict, expect_body: dict):
    """
    校验结果
    :param response_body: 实际结果
    :param expect_body: 预期结果
    :return:
    """
    logging.info("接口响应结果：>>>{}".format(response_body.get('response_body')))
    result = list()
    for key, value in expect_body.items():
        if key.lower() == 'check_json':
            with allure.step("check_json: code校验"):
                allure.attach(name='预期响应码: ', body=str(value.get('expected_code')))
                allure.attach(name='实际响应码: ', body=str(response_body.get('response_code')))
            # expected_code: 200
            if int(value.get('expected_code')) != int(response_body.get('response_code')):
                result.append(False)
                logging.info("请求状态码校验不通过: 预期>>>{} 实际>>>{}".format(value.get('expected_code'),
                                                                  response_body.get('response_code')))
                break
            # 预期结果json文件格式全匹配
            # elif value.get('check_type') == 'perfect_match' or value.get('check_type') == '==':
            #     logging.info("预期结果：{}".format(value.get('expected_result')))
            #     result.append(checkData.check_resp(response_body.get('response_body'), value.get('expected_result')))
            # # 预期结果json文件格式部分匹配
            # elif value.get('check_type') == 'partial_match' or value.get('check_type') == 'in':
            #     pass
            elif value.get('check_type') not in ['perfect_match', '==', 'partial_match', 'in']:
                result.append(False)
                logging.info("预期结果校验方式不存在>>>{}".format(value.get('check_type')))
                break
            else:
                path = APIJSON + '\\' + value.get('expected_result')
                expect_result = read_json(path, is_str=False)
                # TODO
                # ini_params
                # logging.info("预期结果：{}".format(value.get('expected_result')))
                logging.info("预期结果: >>>{}".format(expect_result))
                with allure.step("check_json: data校验"):
                    allure.attach(name='校验方式: ', body=str(value.get('check_type')))
                    allure.attach(name='预期结果: ', body=str(expect_result))
                    allure.attach(name='实际结果: ', body=str(response_body.get('response_body')))
                # result.append(checkData.check_resp(response_body.get('response_body'), value.get('expected_result'),
                #                                    value.get('check_type')))
                result.append(
                    checkData.check_resp(response_body.get('response_body'), expect_result, value.get('check_type')))
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
        'check_json': {
            'check_type': 'partial_match',
            'expected_code': '200',
            'expected_result': 'test.json'},
        'check_2': {'check_type': 'check_db'}}
    reponse_body = {'response_code': 200, 'response_body': {'code': '00000', 'msg': '操作成功'}}
    print(check_res(reponse_body, expect_body))
    pass
