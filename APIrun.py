# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/18 9:01
@file    :APIrun.py
"""
import os

import pytest

# from com.core.replaceData import replace_user_func, replace_func
from com.util import logOperation

if __name__ == "__main__":
    # from com.util.yamlOperation import read_yaml
    from com.util.getFileDirs import LOGS, TESTCASES, REPORT
    from com.util.scriptOperation import write_script
    from com.util.getConfig import Config

    con = Config()

    logOperation.MyLogs(LOGS)

    # 写pytest脚本
    write_script()

    # 定义运行参数
    args_list = ['-vs', TESTCASES,
                 '--reruns', con.get_config('pytest', 'reruns'),
                 '--maxfail', con.get_config('pytest', 'maxfail'),
                 '--alluredir', REPORT + '/xml',
                 '--clean-alluredir',
                 '--disable-warnings']

    test_result = pytest.main(args_list)

    # 生成allure报告
    cmd = 'allure generate --clean %s -o %s ' % (REPORT + '/xml', REPORT + '/html')
    os.system(cmd)
