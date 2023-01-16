# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2023/1/5 11:20
@file    :learn_dataclass.py
"""

from dataclasses import dataclass
from typing import Any, List


# 自定义数据类型
@dataclass()
class Data:
    name: str
    value: Any = 42


data = Data('muzili', value=9)
print(data.name)
print(data.value)


# 自定义嵌套的数据类型
@dataclass()
class InnerData:
    name: str
    age: int
    data: List[Data]


data1 = Data('xiaoli', value=30)

inner = InnerData('liyihong', 18, [data, data1])
print(inner.name)
print(inner.age)
print(inner.data[0].name)
print(inner.data[1].name)
print(inner.data)
print(inner.data[0].value)
print(inner.data[1].value)
print(data.value > data1.value)


# 自定义不可变的数据类型
@dataclass(frozen=True)
class FrozenData:
    name: str
    value: Any = 42


data = FrozenData('muzili', value=9)
print(data.name)
print(data.value)
# data.name = 'xiaoli'  # 报错
