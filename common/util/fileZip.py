# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/25 15:02
@file    :fileZip.py
"""
import os
import zipfile

from common.util.filePath import ensure_path_sep, HISTORYREPORT
from common.util.randomData import get_current_time


def touch_open_report(path: str) -> None:
    """
    创建一个打开报告的脚本
    :param path: 文件存放的路径
    :return:
    """
    cmd = f"""#!/bin/bash

allure open \\html

echo 按任意键继续
read -n 1
echo 继续运行
    """
    filename = ensure_path_sep(path + r'\open_report.sh')
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(cmd)


def make_zip(source_dir: str, output_filename: str = None) -> str:
    """
    打包目录为zip文件(未压缩)
    :param source_dir: 需要压缩的文件名
    :param output_filename: 指定压缩后的文件名
    :return: 返回压缩后的文件名
    """
    if output_filename is None:
        if not os.path.exists(HISTORYREPORT):
            os.makedirs(HISTORYREPORT)
        output_filename = ensure_path_sep(HISTORYREPORT + '\\' + get_current_time() + '.zip')

    with zipfile.ZipFile(output_filename, 'w') as zip_file:
        pre_len = len(os.path.dirname(source_dir))
        touch_open_report(source_dir)
        for parent, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                pathfile = ensure_path_sep(os.path.join(parent, filename))
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zip_file.write(pathfile, arcname)

    return output_filename


def un_zip(file_name: str) -> None:
    """
    解压目录为zip文件
    :param file_name:
    :return:
    """
    with zipfile.ZipFile(file_name) as zip_file:
        if os.path.isdir(file_name + "_files"):
            pass
        else:
            os.mkdir(file_name + "_files")
        for names in zip_file.namelist():
            zip_file.extract(names, file_name + "_files/")


if __name__ == '__main__':
    ...
