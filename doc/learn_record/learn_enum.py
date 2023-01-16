# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2023/1/5 14:05
@file    :learn_enum.py
"""
from enum import Enum, IntEnum, unique


# 继承枚举类
class Color(Enum):
    YELLOW = 1
    BROWN = 1
    # 注意BROWN的值与YELLOW的值相同，这是允许的，此时BROWN相当于YELLOW的别名
    RED = 2
    GREEN = 3
    PINK = 4


print(Color(1).name)
print(Color(2).name)
print(Color(3).name)
print(Color(4).name)

print(Color.YELLOW)  # Color.YELLOW
print(Color.BROWN)  # Color.YELLOW
print(Color.RED)  # Color.RED
print(Color.GREEN)  # Color.GREEN
print(Color.PINK)  # Color.PINK

print(Color.YELLOW.value)
print(Color.BROWN.value)
print(Color.RED.value)
print(Color.GREEN.value)
print(Color.PINK.value)

print(Color(1))  # Color.YELLOW
print(Color(2))
print(Color(3))
print(Color(4))  # Color.PINK
print(Color(1))  # Color.YELLOW


# Color.YELLOW = 7  # 报错


# 1、枚举类不能用例实例化对象
# 2、访问枚举类中的某一项，直接使用类名访问加上要访问的项即可，比如 Color.YELLOW
# 3、枚举类里面定义的 key=value，在类外部不能修改value值，否则会报错
# 4、枚举项可以用来比较，使用 == 或者 is
# 5、导入Enum后，一个枚举类中的key不能相同，value可以相同，相同的value当作key的别名
# 6、如果枚举类中value只能是整型数字，可以使用 IntEnum
# 7、如果要枚举类中的key也不能相同，那么在导入Enum的同时，需要导入unique函数

@unique
class IntColor(IntEnum):
    YELLOW = '1'
    # BROWN = '1'
    # BLUE = 'a' # 报错
    RED = '2'
    PINK = '3'


print(IntColor.RED.value)
# print(IntColor.BROWN.value)
print(IntColor.YELLOW.value)
print(IntColor.PINK.value)
