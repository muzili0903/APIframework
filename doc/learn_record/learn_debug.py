# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2023/1/11 11:08
@file    :learn_debug.py
"""
# Show Execution Point:
# 无论你的代码编辑 窗口的光标在何处,只要点下该按钮,都会自动跳转到程序运行的地方

# Step Over:
# 单步执行, 程序代码越过子函数,但子函数会执行,且不进入

# Step Into:
# 单步执行, 遇到子函数就进入并且继续单步执行, 会跳到源代码里面去执行

# Step Into My Code:
# 单步执行, 遇到子函数就进入并且继续单步执行, 不会跳到源代码里面去执行

# Step Out:
# 跳出当前函数体内, 返回到调用此函数的地方

# Run To Cursor:
# 运行到光标处, 省得每次都要打一个断点

# Evaluate Expression:
# 计算表达式，在里面可以自己执行一些代码

# 一般操作步骤:
# 设置好断点, debug
# F8 单步调试
# 想进入的函数 F7 进入
# 想出来在 shift + F8
# 跳过不想看的地方, 直接设置下一个断点, 然后 F9 过去

# 程序控制菜单
# 重新以 debug 模式运行该程序
# 跳过当前断点 直接运行到下一个断点
# 直接停止运行当前程序
# 显示所有设置的断点
# 使所有断点都失去作用
# 恢复控制台布局


# PyCharm跑完后立即进入调试模式
name = 'muzili'
age = 20
print(name) # 在这里打断点, 程序运行到这里时, 在console 输入 age=18 将会改变 age 的值
print(age)