# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/19 12:15
@file    :initializeParam.py
"""
import random
import re
import logging

from com.core import reqSend


def replace_uservar(case, data):
    """
    替换报文中的用户参数值 ${变量名}
    :param case: 用例报文
    :param data: 用例数据
    :return:
    """
    if re.search('\$\{.*?\}', case).group():
        res = re.findall('\$\{.*?\}', case)
    else:
        return case
    try:
        for i in range(len(res)):
            var = res[i].split('{')[1].split('}')[0]
            case = case.replace(res[i], data[var], 1)
    except KeyError:
        logging.error("获取不到变量值>>>{}".format(var))
    return case


def replace_func(case):
    """
    替换报文中的函数变量值 $(函数名)
    :param case:
    :return:
    """
    pass


def lizi():
    s = "sfasdfa$(t)rere$(t)fdsa$(t)fasdfa$(t)"
    if re.search('\$', s).group():
        res = re.findall('\$\(.*?\)', s)
    else:
        print("d")
    print(res)
    for i in range(len(res)):
        func = eval('reqSend.' + res[i].split('(')[1].split(')')[0] + '()')
        s = s.replace(res[i], func, 1)
    return s


def replace_resp(case, resp_data):
    """
    替换报文中的响应报文参数值 $Resp{变量名}
    :param case:
    :param resp_data:
    :return:
    """
    pass


if __name__ == "__main__":
    from com.util.yamlOperation import read_yaml
    from com.util.getFileDirs import APIYAML

    file = APIYAML + '\\api.yaml'
    case = read_yaml(file)
    d = {"payTaxpayerName": "muzili", "businessNo": "123456"}
    case = replace_uservar(case, d)
    print(case)
    pass
