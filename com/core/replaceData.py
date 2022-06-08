"""
@Time ： 2022/5/19 19:45
@Auth ： muzili
@File ： replaceData.py
@IDE  ： PyCharm
"""
import re
import logging

from jsonpath import jsonpath
from com.util import sysFunc
from api import userFunc
from com.util.glo import GolStatic


def replace_user_var(case, data: dict):
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
        for index in range(len(res)):
            var = res[index].split('{')[1].split('}')[0]
            case = case.replace(res[index], str(data[var]), 1)
    except KeyError:
        logging.error("获取不到变量值: >>>{}".format(var))
    return case


def replace_func(case):
    """
    替换请求报文中的函数变量值 $(f函数名)
    :param case:
    :return:
    """
    if re.search('\$\(f.*?\)', case) is not None:
        res = re.findall('\$\(f.*?\)', case)
    else:
        return case
    try:
        for index in range(len(res)):
            func_params = res[index].split('(', 1)[1].split(')', 1)[0]
            if "::" in func_params:  # 带参函数
                func_name, params = func_params.split("::")
                func = func_name + '(' + params + ')'
            else:  # 不带参函数
                func = func_params + '()'
            func = eval('sysFunc.' + func)
            case = case.replace(res[index], func, 1)
    except AttributeError:
        logging.error("获取不到系统函数: >>>{}".format(func))
    return case


def replace_user_func(case):
    """
    替换请求报文中的函数变量值 $(u函数名)
    :param case:
    :return:
    """
    if re.search('\$\(u.*?\)', case) is not None:
        res = re.findall('\$\(u.*?\)', case)
    else:
        return case
    try:
        for index in range(len(res)):
            func_params = res[index].split('(', 1)[1].split(')', 1)[0]
            if "::" in func_params:  # 带参函数
                func_name, params = func_params.split("::")
                func = func_name + '(' + params + ')'
            else:  # 不带参函数
                func = func_params + '()'
            func = eval('userFunc.' + func)
            case = case.replace(res[index], func, 1)
    except AttributeError:
        logging.error("获取不到自定义函数: >>>{}".format(func))
    return case


def replace_resp(case):
    """
    从其它接口的响应报文中替换请求报文中的参数值 $Resp{接口名.变量名}
    :param case:
    :return:
    """
    if re.search('\$Resp\{.*?\}', case) is not None:
        res = re.findall('\$Resp\{.*?\}', case)
    else:
        return case
    # 测试专用
    # GolStatic.set_file_temp('test', 'response_body',
    #                         {'businessNo': '123456', 'j': [{'businessNo': '1111'}, {'businessNo': '2222'}]})
    try:
        for index in range(len(res)):
            var = res[index].split('{')[1].split('}')[0]
            filename, var_name = var.split('.', 1)
            response_body = GolStatic.get_file_temp(filename=filename, key='response_body')
            value = jsonpath(response_body, var_name)
            if value:
                case = case.replace(res[index], value[0], 1)
            else:
                case = case.replace(res[index], '', 1)
                logging.error("获取不到响应报文字段值: >>>{}".format(var_name))
    except KeyError:
        logging.error("获取不到响应报文字段值: >>>{}".format(var))
    except ValueError:
        logging.error("获取不到变量名: >>>{}".format(var))
    return case


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

    # file = APIYAML + '\\test.yaml'
    # case = read_yaml(file)
    # d = {"payTaxpayerName": "muzili", "businessNo": "123456"}
    # case = replace_uservar(case, d)
    # case = replace_func(case)
    # case = replace_user_func(case)
    # print(case)
    # case = "afafa$(unum)asdf$(fnum::5)aaaa$(fnum::length=10)nbbb"
    # if re.search('\$\(u.*?\)', case) is not None:
    #     res = re.findall('\$\(u.*?\)', case)
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
    case = '{"payTaxpayerName": "${muzili}", "payTaxpayerName": "${muzili}", "businessNo": "$Resp{test.jj[0].businessNo}"}'
    data = {"muzili": '12'}
    print(replace_resp(case))
