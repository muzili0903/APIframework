# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2023/1/10 9:21
@file    :learn_decorator.py
"""


# 普通装饰器
def logger(func):
    def wrapper(*args, **kwargs):
        print('准备执行{}函数:'.format(func.__name__))
        func(*args, **kwargs)
        print('执行函数完毕')

    return wrapper


@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x + y))


add(1, 2)


# 带参数的函数装饰器
def say_hello(contry=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            if contry == 'china':
                print('你好')
            elif contry == 'america':
                print('hello.')
            else:
                return
            func(*args, **kwargs)

        return inner

    return wrapper


@say_hello('china')
def muzili():
    ...


@say_hello('america')
def jack():
    ...


# 用带参数装饰器装饰时, 参数必传, 不传会报错
# 用带参数装饰器装饰时, 参数有默认值, 可以不传, 但是后面的say_hello()不能省略
@say_hello()
def xiaoli():
    ...


muzili()
jack()
xiaoli()


# 不带参数的类装饰器
class Logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('类装饰器: func={}()'.format(self.func.__name__))
        return self.func(*args, **kwargs)


@Logger
def say(something):
    print("say {} !".format(something))
    return 1


say('hello')


# 带参数的类装饰器
class Loggers(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('[{}]: the function {}() is running...'.format(self.level, func.__name__))
            func(*args, **kwargs)

        return wrapper


@Loggers(level='WARNING')
def says(something):
    print('says {} !'.format(something))


says('hello')

# 使用偏函数与类实现装饰器
import time
import functools


class DelayFunc(object):
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print('wait for {} seconds...'.format(self.duration))
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('call without delay')
        return self.func(*args, **kwargs)


def delay(duration):
    """
    装饰器: 推迟某个函数的执行
    同时提供 eager_call 方法立刻执行
    :param duration:
    :return:
    """
    # 此时为了避免定义额外函数
    # 直接使用偏函数帮助构建 DelayFunc 实例
    return functools.partial(DelayFunc, duration)


@delay(duration=2)
def adds(a, b):
    return a + b


print(adds(1, 2))
print(type(adds))
print(type(adds.func))

# 能装饰类的类装饰器
# 实现单例模式
instances = {}


def singleton(cls):
    def get_instance(*args, **kwargs):
        cls_name = cls.__name__
        print('--------1---------')
        if not cls_name in instances:
            print('--------2---------')
            instance = cls(*args, **kwargs)
            instances[cls_name] = instance
        return instances[cls_name]

    return get_instance


@singleton
class User:

    def __init__(self, name, age):
        print('--------3---------')
        self.name = name
        self.age = age


@singleton
class Person:
    def __init__(self, name, age):
        print('--------3---------')
        self.name = name
        self.age = age


user = User('muzili', 18)
print(user.name)
print(user.age)
user1 = User('xiaoli', 20)
print(user1.name)
print(user1.age)
person = Person('muzili', 18)
print(person.name)
print(person.age)
person1 = Person('xiaoli', 20)
print(person1.name)
print(person1.age)


# 能装饰类成员方法的类装饰器
def wrapper(obj):
    def inner(self):
        obj(self)
        print('这是类成员方法的类装饰器')
        return self.func  # 装饰类中的func方法

    return inner
