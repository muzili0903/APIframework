# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/25 14:41
@file    :openHistoryReport.py
"""
import os

from common.util.filePath import ensure_path_sep, HISTORYREPORT
from common.util.fileZip import un_zip


def open_report(zip_name: str) -> None:
    """
    打开历史allure报告
    :param zip_name: allure报告压缩后的zip文件名
    :return:
    """
    path = ensure_path_sep(HISTORYREPORT + '\\' + zip_name)
    un_zip(path)
    cmd = ensure_path_sep(f'allure open {path}' + r'_files\report\html')
    os.system(cmd)


if __name__ == '__main__':
    open_report(r'20230530162549.zip')
