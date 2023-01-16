# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2023/1/6 16:37
@file    :learn_types.py
"""
import asser_type
import types

# print(isinstance(100, types.FunctionType))
# print(dir(types))
from typing import Dict, Text, Callable, Any


class Foo(object):
    def run(self):
        return None


def bark(self):
    print(11111)
    return None


print(isinstance(Foo.run, types.FunctionType))
print(isinstance(Foo().run, types.MethodType))
fun = Foo().run

# MethodType动态的给对象添加实例方法
a = Foo()
a.bark = types.MethodType(bark, a)
a.bark()


def load_module_functions(module) -> Dict[Text, Callable]:
    """ 获取 module中方法的名称和所在的内存地址 """
    module_functions = {}

    for name, item in vars(module).items():
        print('name: ', name)
        print('item: ', item)
        if isinstance(item, types.FunctionType):
            module_functions[name] = item
    return module_functions


module_functions = load_module_functions(asser_type)
module_functions['equals'](1, 2, '不相等')


def res_sql_data_bytes(res_sql_data: Any) -> Text:
    """ 处理 mysql查询出来的数据类型如果是bytes类型，转换成str类型 """
    if isinstance(res_sql_data, bytes):
        res_sql_data = res_sql_data.decode('utf=8')
    return res_sql_data
