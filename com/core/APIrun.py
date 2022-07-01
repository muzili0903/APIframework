# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/24 22:51
@Auth ： muzili
@File ： APImain.py
@IDE  ： PyCharm
"""
import os
# import multiprocessing
# from multiprocessing import Lock

import pytest

from com.util import logOperation
from com.util.fileOperation import json_to_yaml, make_zip
from com.util.getFileDirs import LOGS, TESTCASES, REPORT
from com.util.scriptOperation import write
from com.util.mailOperation import send_mail
from com.util.getConfig import Config


def run():
    # 获取配置文件
    con = Config()

    logOperation.MyLogs(LOGS)

    # 将api文件夹中的 json文件格式转为yaml文件格式
    if eval(con.get_config('API', 'json_to_yaml').capitalize()):
        json_to_yaml(con)

    # 写pytest脚本
    if eval(con.get_config('TESTCASES', 'script_refresh').capitalize()):
        write(con)

    # 定义运行参数
    args_list = ['-vs', TESTCASES,
                 '--reruns', con.get_config('pytest', 'reruns'),
                 '--reruns-delay', con.get_config('pytest', 'delay'),
                 '--maxfail', con.get_config('pytest', 'maxfail'),
                 '-n', con.get_config('pytest', 'gip'),
                 '--dist=loadfile',
                 '--alluredir', REPORT + '/xml',
                 '--clean-alluredir',
                 '--disable-warnings']

    pytest.main(args_list)

    # 生成allure报告
    cmd = 'allure generate --clean %s -o %s ' % (REPORT + '/xml', REPORT + '/html')
    os.system(cmd)

    # 打包报告文件放在history目录下
    report_zip = make_zip(REPORT)
    # 发送邮件
    if eval(con.get_config('mail', 'is_send_mail').capitalize()):
        send_mail(con, report_zip)


if __name__ == "__main__":
    pass
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
