# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/18 9:01
@file    :APIrun.py
"""
import multiprocessing
from multiprocessing import Lock

if __name__ == "__main__":
    import os

    import pytest

    from com.util import logOperation
    from com.util.fileOperation import json_to_yaml, get_all_file
    from com.util.getFileDirs import LOGS, TESTCASES, REPORT, APISCENE
    from com.util.scriptOperation import write
    from com.util.getConfig import Config

    con = Config()

    logOperation.MyLogs(LOGS)

    # 将api文件夹中的 json文件格式转为yaml文件格式
    if con.get_config('API', 'json_to_yaml'):
        json_to_yaml(con)

    # 写pytest脚本
    if con.get_config('TESTCASES', 'script_refresh'):
        write(con)

    # 引入多进程
    # scene_script_list = get_all_file(APISCENE)
    # lock = Lock()
    # for scene_script_path in scene_script_list:
    #     file_path = TESTCASES + scene_script_path.rsplit('\\', 1)[1] + '\\'
    #     args = ['-vs', file_path,
    #              '--reruns', con.get_config('pytest', 'reruns'),
    #              '--reruns-delay', con.get_config('pytest', 'delay'),
    #              '--maxfail', con.get_config('pytest', 'maxfail'),
    #              '--alluredir', REPORT + '/xml',
    #              '--clean-alluredir',
    #              '--disable-warnings']
    #     process = multiprocessing.Process(target=pytest.main, args=(lock, args))
    #     process = multiprocessing.Process(target=pytest.main, args=(args, ))
    #     process.start()
    # 定义运行参数
    args_list = ['-vs', TESTCASES,
                 '--reruns', con.get_config('pytest', 'reruns'),
                 '--reruns-delay', con.get_config('pytest', 'delay'),
                 '--maxfail', con.get_config('pytest', 'maxfail'),
                 '--alluredir', REPORT + '/xml',
                 '--clean-alluredir',
                 '--disable-warnings']

    test_result = pytest.main(args_list)

    # 生成allure报告
    cmd = 'allure generate --clean %s -o %s ' % (REPORT + '/xml', REPORT + '/html')
    os.system(cmd)
