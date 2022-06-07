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
    from com.util.getFileDirs import APIYAML, LOGS, TESTCASES
    from com.util.scriptOperation import write_script

    logOperation.MyLogs(LOGS)

    write_script()

    # 定义运行参数
    args_list = ['-vs', TESTCASES,
                 # '-n', str(RC['process']),
                 # '--reruns', str(RC['reruns']),
                 # '--maxfail', str(RC['maxfail']),
                 # '--alluredir', REPORT_DIR + '/xml',
                 '--clean-alluredir',
                 '--disable-warnings']
    # 判断是否开启用例匹配
    # if RC['pattern']:
    #     args_list += ['-k ' + str(RC['pattern'])]
    test_result = pytest.main(args_list)
