# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/3 13:28
@Auth ： muzili
@File ： fieldsDispose.py
@IDE  ： PyCharm
"""
import math

from com.util.sysFunc import fnum


def dispose_int(field: dict):
    normal_value = list()
    abnormality_value = list()
    default = None
    if field.get('isRequired') is None or field.get('isRequired').__eq__('N'):
        # 字段正常案例校验
        value = {
            'title': '{} 字段为空'.format(field.get('field')),
            field.get('field'): '',
        }
        normal_value.append(value)
        value = {
            'title': '{} 字段不传'.format(field.get('field')),
            field.get('field'): None,
        }
        normal_value.append(value)
        value = {
            'title': '{} 字段输入正确的最大值'.format(field.get('field')),
            field.get('field'): math.pow(10, field.get('length')) - 1,
        }
        normal_value.append(value)
        value = {
            'title': '{} 字段输入正确的最小值'.format(field.get('field')),
            field.get('field'): 0,
        }
        normal_value.append(value)

        # 字段异常案例校验
        value = {
            'title': '{} 字段输入超长的值'.format(field.get('field')),
            field.get('field'): math.pow(10, field.get('length')),
        }
        abnormality_value.append(value)
        value = {
            'title': '{} 字段输入类型错误'.format(field.get('field')),
            field.get('field'): fnum(int(field.get('length'))),
        }
        abnormality_value.append(value)
    else:
        # 字段正常案例校验
        value = {
            'title': '{} 字段输入正确的最大值'.format(field.get('field')),
            field.get('field'): math.pow(10, field.get('length')) - 1,
        }
        normal_value.append(value)
        value = {
            'title': '{} 字段输入正确的最小值'.format(field.get('field')),
            field.get('field'): 0,
        }
        normal_value.append(value)

        # 字段异常案例校验
        value = {
            'title': '{} 字段输入超长的值'.format(field.get('field')),
            field.get('field'): math.pow(10, field.get('length')),
        }
        abnormality_value.append(value)
        value = {
            'title': '{} 字段输入类型错误'.format(field.get('field')),
            field.get('field'): fnum(int(field.get('length'))),
        }
        abnormality_value.append(value)
        value = {
            'title': '{} 字段为空'.format(field.get('field')),
            field.get('field'): '',
        }
        abnormality_value.append(value)
    if field.get('default') is not None:
        default = {
            'title': '{} 字段默认值'.format(field.get('field')),
            field.get('field'): field.get('default'),
        }
    return {'normal_value': normal_value, 'abnormality_value': abnormality_value, 'default': default}


def dispose_float(field: dict):
    pass


def dispose_string(field: dict):
    pass


def dispose_list(field: dict):
    pass


def dispose_object(field: dict):
    pass


if __name__ == "__main__":
    field = {
        'field': 'id',
        'type': int,
        'length': 8,
        'default': 32,
        'isRequired': 'Y'
    }
    fields = dispose_int(field)
    print(fields)
