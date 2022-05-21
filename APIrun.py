# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/18 9:01
@file    :APIrun.py
"""
import pytest

from com.core.replaceData import replace_user_func, replace_func
from com.util import logOperation

if __name__ == "__main__":
    from com.util.yamlOperation import read_yaml
    from com.util.getFileDirs import APIYAML, LOGS

    logOperation.MyLogs(LOGS)

    file = APIYAML + '\\test.yaml'
    case = read_yaml(file)
    d = {"payTaxpayerName": "muzili", "businessNo": "123456"}
    case = replace_user_func(case)
    case = replace_func(case)
    print(case)
