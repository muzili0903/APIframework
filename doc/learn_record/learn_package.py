# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2023/1/11 10:53
@file    :learn_package.py
"""
# 在module中使用 __all__ 可以控制被其它模块导入的变量
name = 'muzili'
age = 18

__all__ = ['name']

# pip 使用指南
# 查询当前环境按照的所有软件包
# pip list
# 查询当前环境可以升级的包
# pip list --outdated
# 查询一个包的详情内容
# pip show package
# 安装非二进制的包
# pip install package --no-binary
# 指定代理服务器安装
# pip install --proxy [user:password@]http_server_ip:port package
# 卸载软件包
# pip uninstall package
# 升级软件包
# pip install --upgrade package

