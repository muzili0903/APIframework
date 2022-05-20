# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/19 12:15
@file    :initializeParam.py
"""
import random
import re
import logging

from com.util import userFunc


def replace_uservar(case, data):
    """
    替换请求报文中的用户参数值 ${变量名}
    :param case: 用例报文
    :param data: 用例数据
    :return:
    """
    if re.search('\$\{.*?\}', case) is not None:
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
    替换请求报文中的函数变量值 $(函数名)
    :param case:
    :return:
    """
    if re.search('\$\(.*?\)', case) is not None:
        res = re.findall('\$\(.*?\)', case)
    else:
        return case
    try:
        for i in range(len(res)):
            func_param = res[i].split('(', 1)[1].split(')', 1)[0]
            if "::" in func_param:  # 带参函数
                funcName, param = func_param.split("::")
                func = funcName + '(' + param + ')'
            else:  # 不带参函数
                func = func_param + '()'
            func = eval('userFunc.' + func)
            case = case.replace(res[i], func, 1)
    except AttributeError:
        logging.error("获取不到函数>>>{}".format(func))
    return case


def replace_resp(case, resp_data):
    """
    从其它接口的响应报文中替换请求报文中的参数值 $Resp{变量名}
    :param case:
    :param resp_data:
    :return:
    """
    pass


def replace_req(case, req_data):
    """
    从其它接口的请求报文中替换请求报文中的参数值 $Req{变量名}
    :param case:
    :param req_data:
    :return:
    """
    pass


def replace_db(case):
    """
    从其它接口的请求报文中替换请求报文中的参数值 $DB{变量名}
    :param case:
    :return:
    """
    pass


if __name__ == "__main__":
    from com.util.yamlOperation import read_yaml
    from com.util.getFileDirs import APIYAML

    file = APIYAML + '\\test.yaml'
    case = read_yaml(file)
    d = {"payTaxpayerName": "muzili", "businessNo": "123456"}
    # case = replace_uservar(case, d)
    case = replace_func(case)
    print(case)
    # case = "afafa$(fdate)asdf$(fnum::5, 2)aaaa$(fnum::n=5,length=10)nbbb"
    # if re.search('\$\(.*?\)', case) is not None:
    #     res = re.findall('\$\(.*?\)', case)
    #     print(res)
    # else:
    #     print("case:", case)
    # for i in range(len(res)):
    #     func_param = res[i].split('(', 1)[1].split(')', 1)[0]
    #     if "::" in func_param:
    #         funcName, param = func_param.split("::")
    #         func = funcName + '(' + param + ')'
    #     else:
    #         func = func_param + '()'
    #     func = eval('userFunc.' + func)
    #     case = case.replace(res[i], func, 1)
    #     print(case)
    pass
