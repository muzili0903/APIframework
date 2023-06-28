# -*- coding: utf-8 -*-
"""
@Author  :muzili
@time    :2023/6/26 11:14
@file    :retryRequests.py
"""
import threading
import time

from common.util.globalVars import GolStatic
from common.util.logOperation import logger

proConfig = GolStatic.get_pro_var('PROCONFIG')
retry_number = proConfig.get_config_int('RETRY', 'number')
sleeptime = proConfig.get_config_int('RETRY', 'sleeptime')


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


def repeated_requests(func):
    """
    被装饰的函数func返回值必须是bool类型
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        logger.info('进入wrapper')
        funcQueue = GolStatic.get_pro_var('funcQueue')
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
                logger.info('再次进入wrapper')
                time.sleep(sleeptime)
                thr = MyThread(func, *args, **kwargs)
                funcQueue.put(thr)
                count_func[func] += 1

    return wrapper


if __name__ == '__main__':
    pass
