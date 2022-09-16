# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2022/9/13 14:39
@file    :myThread.py
"""
import threading
import time

from com.util.logOperation import funcQueue
from com.util.getConfig import Config

sleeptime = int(Config().get_config_int('RETRY', 'sleeptime'))
retry_number = int(Config().get_config_int('RETRY', 'number'))


class MyThread(threading.Thread):
    def __init__(self, func, *args, **kwargs):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.flag = True

    def run(self):
        self.result = self.func(*self.args, **self.kwargs)

    def get_result(self):
        threading.Thread.join(self)  # 等待线程执行完毕
        try:
            return self.result
        except Exception:
            return None

    def set_flag(self, flag=False):
        self.flag = flag


def async_wait(func):
    def wrapper(*args, **kwargs):
        thr = MyThread(func, *args, **kwargs)
        funcQueue.put(thr)
        count_func = {func: 1}
        while not funcQueue.empty():
            function = funcQueue.get(True, .5)
            function.start()
            if function.get_result() is None:  # 被装饰的函数func返回None或断言失败,抛出断言失败让pytest捕获
                raise AssertionError('断言失败或返回None')
            if function.get_result():  # 被装饰的函数func返回True,重推
                if count_func.get(func).__eq__(retry_number):  # 限制重推次数
                    raise AssertionError('超过重推次数')
                time.sleep(sleeptime)
                thr = MyThread(func, *args, **kwargs)
                funcQueue.put(thr)
                count_func[func] += 1

    return wrapper


if __name__ == '__main__':
    pass
