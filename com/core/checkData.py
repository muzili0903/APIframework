# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/26 12:24
@file    :checkData.py
"""
import logging

from com.core import replaceData


def check_req(response_body: dict, expect_body: dict):
    pass


def check_list(response_body: list, expect_body: list, check_type) -> bool:
    """
    校验列表字段值
    :param response_body: 响应结果
    :param expect_body: 预期结果
    :param check_type:
    :return:
    """
    result = True
    if check_type in ['perfect_match', '==']:
        if response_body.__len__() != expect_body.__len__():
            result = False
            return result
    try:
        for index, value in enumerate(expect_body):
            if isinstance(value, dict):
                result = check_resp(response_body[index], value, check_type)
                response_body.remove(value)
                expect_body.remove(value)
            elif isinstance(value, list):
                result = check_list(response_body[index], value, check_type)
                response_body.remove(value)
                expect_body.remove(value)
            else:
                # if isinstance(value, str):
                #     if str(value) == str(response_body[index]):
                #         result = True
                #     else:
                #         result = False
                if value in response_body:
                    response_body.remove(value)
                    expect_body.remove(value)
                # else:
                #     if value == response_body:
                #         response_body.remove(value)
                #         expect_body.remove(value)
                #     else:
                #         result = False
        else:
            if check_type in ['perfect_match', '==']:
                if response_body.__len__() != expect_body.__len__():
                    result = False
                    return result
                else:
                    result = True
                    return result
    except Exception as e:
        result = False
        logging.info("JSON格式校验，预期结果{}与响应结果{}值不一致".format(expect_body, response_body))
        logging.info("值校验报错{}".format(e))
    return result


def check_resp(response_body: dict, expect_body: dict, check_type) -> bool:
    """
    校验响应报文，预期结果json文件格式
    :param response_body:
    :param expect_body:
    :param check_type:
    :return:
    check_type: perfect_match
    expected_result: test_response.json
    """
    resp = False
    if isinstance(expect_body, dict):
        for key, value in expect_body.items():
            if key not in response_body:
                logging.info("JSON格式校验，关键字{}不在响应结果{}中".format(key, response_body))
                return resp
            else:
                if isinstance(value, dict) and isinstance(response_body.get(key), dict):
                    resp = check_resp(value, response_body.get(key), check_type)
                elif not isinstance(value, type(response_body.get(key))):
                    logging.info("JSON格式校验，关键字{}预期结果{}与响应结果{}类型不符".format(key, value, response_body.get(key)))
                    return resp
                else:
                    if isinstance(value, list):
                        resp = check_list(response_body.get(key), value, check_type)
                    else:
                        if str(value) == str(response_body.get(key)):
                            resp = True
                        else:
                            resp = False
    else:
        logging.info("JSON校验内容非dict格式：{}".format(expect_body))
        return resp
    return resp


def check_db(response_body: dict, expect_body: dict) -> bool:
    return True


if __name__ == "__main__":
    # test {'test': {"test": 1}} {'test': [1]]}}
    test = {'test': [{"test1": 2}, {"test": [3]}]}
    test1 = {'test': [{"test1": 2}, {"test": [33]}]}
    test2 = {'test1': 3, 'test2': "22"}
    test3 = {'test1': 33, 'test2': "22"}
    # bug 待解决
    print(check_resp(test, test1, 'partial_match'))
    print(check_resp(test2, test3, 'partial_match'))
    pass
