# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2023/1/10 15:11
@file    :learn_class.py
"""


# 类的多态
class People:
    def speak(self): ...


class American(People):
    def speak(self):
        print('say hello')


class Chinese(People):
    def speak(self):
        print('你好')


american = American()
chinese = Chinese()
american.speak()
chinese.speak()


def speak(people):
    people.speak()


speak(american)
speak(chinese)


# Mixin设计模式
# 责任明确: 必须表示某一种功能, 而不是某个物品
# 功能单一: 若有多个功能, 那就写多个Mixin类
# 绝对独立: 不能依赖于子类的实现, 子类即使没有继承这个Mixin类, 也照样可以工作
class Vehicle(object): ...


class PlaneMixin(object):
    def fly(self):
        print('I am flying')


class Airplane(Vehicle, PlaneMixin): ...


# 类的魔术方法
# 构造方法:
# __init__ 和 __new__ 是对象构造器, __del__ 是对象销毁器
# 实例化对象的时候, 第一个调用的魔术方法是 __new__ 而不是 __init__
# 比较操作符:
# __cmp__(self, other) 定义了所有比较操作符的行为(<,==,!=,等等)
# __eq__(self, other) 定义等于操作符(==)的行为
# __ne__(self, other) 定义不等于操作符(!=)的行为
# __lt__(self, other) 定义小于操作符(<)的行为
# __gt__(self, other) 定义大于操作符(>)的行为
# __ge__(self, other) 定义大于等于操作符(>=)的行为
# 数值操作符:
# __pos__(self) 实现取正操作, 例如 +some_object
# __neg__(self) 实现取负操作，例如 -some_object
# __abs__(self) 实现内建绝对值函数 abs() 操作
# __invert__(self) 实现取反操作符 ~
# __round__(self, n) 实现内建函数 round(),n 是近似小数点的位数
# __floor__(self) 实现 math.floor() 函数，即向下取整
# __ceil__(self) 实现 math.ceil() 函数，即向上取整
# __trunc__(self) 实现 math.trunc() 函数，即截断整数
# 算数操作符:
# 以下魔术方法在方法名前加个 r, 代表反射算数操作符 例如: __radd__(self, other) 相当于 x + y ->  y + x
# 以下魔术方法在方法名前加个 i, 代表增强赋值操作符 例如: __iadd__(self, other) 相当于 x = x + 1 -> x += 1
# __add__(self, other) 实现加法操作
# __sub__(self, other) 实现减法操作
# __mul__(self, other) 实现乘法操作
# __floordiv__(self, other) 实现使用 // 操作符的整数除法
# __div__(self, other) 实现使用 / 操作符的除法
# __truediv__(self, other) 实现 true 除法，这个函数只有使用 from __future__ import division 时才有作用
# __mod__(self, other) 实现 % 取余操作
# __divmod(self, other) 实现 divmod 内建函数
# __pow__(self) 实现 ** 操作符
# __lshift__(self, other) 实现左移位运算符 <<
# __rshift__(self, other) 实现左移位运算符 <<
# __and__(slef, other) 实现按位与运算符 &
# __or__(self, other) 实现按位或运算符 |
# __xor__(self, other) 实现按位异或运算符 ^
# 类型转换操作符
# __int__(self) 实现到int的类型转换
# __long__(self) 实现到long的类型转换
# __float__(self) 实现到float的类型转换
# __complex__(self) 实现到complex的类型转换
# __oct__(self) 实现到八进制数的类型转换
# __hex__(self) 实现到十六进制数的类型转换
# __index__(self) 实现当对象用于切片表达式时到一个整数的类型转换
# 访问控制
# __getattr__(self, name) 当用户试图访问一个根本不存在（或者暂时不存在）的属性时，你可以通过这个魔法方法来定义类的行为
# __setattr__(self, name, value) 它允许你自定义某个属性的赋值行为，不管这个属性存在与否，就是说你可以对任意属性的任何变化都定义自己的规则
# __delattr__(self, name) 它是用于处理删除属性时的行为

class Attr:
    def __setattr__(self, key, value):
        setattr(Attr, key, value)

    def __delattr__(self, item):
        delattr(Attr, item)

    def __getattr__(self, item):
        return getattr(Attr, item)


# a = Attr()
# a.name = 'muzili111111'
# a.name1 = '34'
# print(a.name)
# print(a.name1)
# del a.name1
# print(a.name)
# print(a.name1)

# 容器背后的魔法方法
# __len__(self) 返回容器的长度
# __getitem__(self, key) 定义对容器中某一项使用 self[key] 的方式进行读取操作时的行为
# __setitem__(self, key) 定义对容器中某一项使用 self[key] 的方式进行赋值操作时的行为
# __iter__(self, key) 它应该返回当前容器的一个迭代器
# __reversed__(self) 定义了对容器使用 reversed() 内建函数时的行为
# __contains__(self, item) 定义了使用 in 和 not in 进行成员测试时类的行为
# __missing__(self, item) 在字典的子类中使用，它定义了当试图访问一个字典中不存在的键时的行为(目前为止是指字典的实例，例如我有一个字典 d,
# “george” 不是字典中的一个键，当试图访问 d[“george’] 时就会调用 d.__missing__(”george”))
class FunctionalList:
    '''
    一个列表的封装类, 实现了一些额外的函数式方法
    '''

    def __init__(self, values=None):
        if values is None:
            self.values = list()
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        # 如果键的类型或值不合法, 列表会返回异常
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)

    def head(self):
        # 获取第一个元素
        return self.values[0]

    def tail(self):
        # 获取除第一个元素外的所有元素
        return self.values[1:]


func = FunctionalList()
func.append(1)
func.append(2)
func.append(3)
func.append(4)
print(func.head())
print(func.tail())


# 上下文管理器
# __enter__(self) 注意 __enter__ 的返回值会赋给 with 声明的目标，也就是 as 之后的东西
# __exit__(self, exception_type, exception_value, traceback)

class Closer:
    '''一个上下文管理器, 可以在with语句中
    使用close()自动关闭对象'''

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self, obj):
        return self.obj  # 绑定到目标

    def __exit__(self, exception_type, exception_value, traceback):
        try:
            self.obj.close()
        except AttributeError:  # obj不是可关闭的
            print('Not closable.')
            return True  # 成功地处理了异常
