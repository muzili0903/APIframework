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
    """
    处理int类型的字段
    :param field:
    :return:
    """
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
    """
    处理float类型的字段
    :param field:
    :return:
    """
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
        decade, quantile = str(field.get('length')).split('.')
        normal_value.append(value)
        value = {
            'title': '{} 字段输入正确的最大值'.format(field.get('field')),
            field.get('field'): math.pow(10, int(decade)) - math.pow(10, -int(quantile)),
        }
        normal_value.append(value)
        value = {
            'title': '{} 字段输入正确的最小值'.format(field.get('field')),
            field.get('field'): math.pow(10, -int(quantile)),
        }
        normal_value.append(value)

        # 字段异常案例校验
        value = {
            'title': '{} 字段输入超长的值'.format(field.get('field')),
            field.get('field'): math.pow(10, int(decade)) + math.pow(10, -int(quantile)),
        }
        abnormality_value.append(value)
        value = {
            'title': '{} 字段输入类型错误'.format(field.get('field')),
            field.get('field'): fnum(int(field.get('length'))),
        }
        abnormality_value.append(value)
    else:
        # 字段正常案例校验
        decade, quantile = str(field.get('length')).split('.')
        value = {
            'title': '{} 字段输入正确的最大值'.format(field.get('field')),
            field.get('field'): math.pow(10, int(decade)) - math.pow(10, -int(quantile)),
        }
        normal_value.append(value)
        value = {
            'title': '{} 字段输入正确的最小值'.format(field.get('field')),
            field.get('field'): math.pow(10, -int(quantile)),
        }
        normal_value.append(value)

        # 字段异常案例校验
        value = {
            'title': '{} 字段为空'.format(field.get('field')),
            field.get('field'): '',
        }
        abnormality_value.append(value)
        value = {
            'title': '{} 字段不传'.format(field.get('field')),
            field.get('field'): None,
        }
        abnormality_value.append(value)
        value = {
            'title': '{} 字段输入超长的值'.format(field.get('field')),
            field.get('field'): math.pow(10, int(decade)) + math.pow(10, -int(quantile)),
        }
        abnormality_value.append(value)
        value = {
            'title': '{} 字段输入类型错误'.format(field.get('field')),
            field.get('field'): fnum(int(field.get('length'))),
        }
        abnormality_value.append(value)
    if field.get('default') is not None:
        default = {
            'title': '{} 字段默认值'.format(field.get('field')),
            field.get('field'): field.get('default'),
        }
    return {'normal_value': normal_value, 'abnormality_value': abnormality_value, 'default': default}


def dispose_string(field: dict):
    """
    处理string类型的字段
    :param field:
    :return:
    """
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
            field.get('field'): fnum(int(field.get('length'))),
        }
        normal_value.append(value)

        # 字段异常案例校验
        value = {
            'title': '{} 字段输入超长的值'.format(field.get('field')),
            field.get('field'): fnum(int(field.get('length') + 1)),
        }
        abnormality_value.append(value)
    else:
        # 字段正常案例校验
        value = {
            'title': '{} 字段输入正确的最大值'.format(field.get('field')),
            field.get('field'): fnum(int(field.get('length'))),
        }
        normal_value.append(value)

        # 字段异常案例校验
        value = {
            'title': '{} 字段为空'.format(field.get('field')),
            field.get('field'): '',
        }
        abnormality_value.append(value)
        value = {
            'title': '{} 字段不传'.format(field.get('field')),
            field.get('field'): None,
        }
        abnormality_value.append(value)
        value = {
            'title': '{} 字段输入超长的值'.format(field.get('field')),
            field.get('field'): fnum(int(field.get('length') + 1)),
        }
        abnormality_value.append(value)
    if field.get('default') is not None:
        default = {
            'title': '{} 字段默认值'.format(field.get('field')),
            field.get('field'): field.get('default'),
        }
    return {'normal_value': normal_value, 'abnormality_value': abnormality_value, 'default': default}


def dispose_list(field: dict):
    """
    处理list类型的字段
    :param field:
    :return:
    """
    pass


def dispose_object(field: dict):
    """
    处理object类型的字段
    :param field:
    :return:
    """
    pass


if __name__ == "__main__":
    print(math.pow(10, 2) + math.pow(10, -2))
    print(math.pow(10, 2) - math.pow(10, -0))