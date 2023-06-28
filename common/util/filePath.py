# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/25 14:49
@file    :filePath.py
"""
import os


def ensure_path_sep(path: str) -> str:
    """
    兼容 windows 和 linux 不同环境的操作系统路径
    :param path: 路径
    :return: 路径
    """
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))
    return path


# 基本路径
BASEDIR = ensure_path_sep(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# 项目配置文件路径
CONFDIR = ensure_path_sep(os.path.join(BASEDIR, 'config\config.ini'))
CONFDIRENV = ensure_path_sep(os.path.join(BASEDIR, 'config\\'))

# 报告文件路径
REPORT = ensure_path_sep(os.path.join(BASEDIR, "report"))

# 历史报告文件路径
HISTORYREPORT = ensure_path_sep(ensure_path_sep(os.path.join(BASEDIR, 'historyReport')))

# 日志文件所在目录
LOGS = ensure_path_sep(os.path.join(BASEDIR, "logs"))

# 测试用例所在目录
TESTCASE = ensure_path_sep(os.path.join(BASEDIR, "testCase"))

# 测试数据所在目录
TESTDATA = ensure_path_sep(os.path.join(BASEDIR, "testData"))

if __name__ == '__main__':
    ...
