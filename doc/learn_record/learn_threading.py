# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2023/1/11 14:38
@file    :learn_threading.py
"""
import math
from collections.abc import Coroutine, Generator
import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import currentThread
from queue import Queue
import random
import threading
import time
from multiprocessing import Process
from threading import Thread

import requests


# CPU 计算密集型
def count(x=1, y=1):
    c = 0
    while c < 500000:
        c += 1
        x += x
        y += y


# 磁盘续写IO密集型
def io_disk():
    with open('file.txt', 'w') as f:
        for i in range(500000):
            f.write('python-learning\n')


# 网络IO密集型
header = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.baidu.com'


def io_request():
    try:
        webPage = requests.get(url, headers=header)
        html = webPage.text
        return
    except Exception as e:
        return {'error': e}


# 模拟IO密集型
def io_simulation():
    time.sleep(2)


# 时间计数器
def timer(mode):
    def wrapper(func):
        def inner(*args, **kwargs):
            Type = kwargs.setdefault('Type', None)
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            count_time = end - start
            print("{}-{}花费时间: {}".format(mode, Type, count_time))

        return inner

    return wrapper


@timer('[单线程]')
def signle_thread(func, Type):
    for i in range(10):
        func()


# signle_thread(count, Type='CPU计算密集型')
# signle_thread(io_simulation, Type='模拟IO密集型')
# [单线程]-CPU计算密集型花费时间: 51.39357328414917
# [单线程]-模拟IO密集型花费时间: 20.074243545532227

@timer(['多线程'])
def multi_thread(func, Type):
    thread_list = list()
    for i in range(10):
        t = Thread(target=func, args=())
        thread_list.append(t)
        t.start()

    length = len(thread_list)

    while True:
        for thread in thread_list:
            if not thread.is_alive():
                length -= 1
        if length <= 0:
            break


# multi_thread(count, Type='CPU计算密集型')
# multi_thread(io_simulation, Type='模拟IO密集型')
# ['多线程']-CPU计算密集型花费时间: 32.2395293712616
# ['多线程']-模拟IO密集型花费时间: 6.786544322967529

@timer(['多进程'])
def multi_process(func, Type):
    process_list = list()
    for i in range(10):
        process = Process(target=func, args=())
        process_list.append(process)
        process.start()

    length = len(process_list)

    while True:
        for process in process_list:
            if not process.is_alive():
                length -= 1
        if length <= 0:
            break


# if __name__ == '__main__':
#     multi_process(count, Type='CPU计算密集型')
#     multi_process(io_simulation, Type='模拟IO密集型')
#     # ['多进程'] - CPU计算密集型花费时间: 6.981333494186401
#     # ['多进程'] - 模拟IO密集型花费时间: 3.9085493087768555
#
#     # 总结
#     # 单线程总是最慢的
#     # 多进程总是最快的
#     # 多进程虽然最快, 但不一定是最优的选择, 因为它需要CPU资源支持下才能体现优势


# =====================================【创建多线程的方法】=====================================
# 用函数创建多线程
def target(name='python'):
    for i in range(2):
        print('hello ', name)
        time.sleep(2)


# 创建线程1, 不指定参数
thread_1 = Thread(target=target)
# 启动线程
# thread_1.start()

# 创建线程2, 指定参数, 注意逗号
thread_2 = Thread(target=target, args=('java',))


# thread_2.start()


class MyThread(Thread):
    # 用类创建多线程
    def __init__(self, name='python'):
        super(MyThread, self).__init__()
        self.name = name

    def run(self) -> None:
        for i in range(2):
            print('hello ', self.name)
            time.sleep(2)


# # 不指定参数
# thread_3 = MyThread()
# # 指定参数
# thread_4 = MyThread('java')
# thread_3.start()
# thread_3.join()
# thread_4.start()
# thread_4.join()
#
# # 线程对象的方法
# # 启动子线程
# thread_4.start()
# # 阻塞子线程, 待子线程结束后, 再往下执行
# thread_4.join()
# # 判断线程是否在执行, 在执行返回 True
# thread_4.is_alive()
# # 判断线程是否随主线程退出而退出, 默认 False
# thread_4.daemon = True
# # 设置线程名
# thread_4.name = 'my-thread'
# =====================================【创建多线程的方法】=====================================


# =====================================【多线程的锁机制】=====================================
# 互斥锁
# 生成锁对象, 全局唯一
lock = threading.Lock()


# 获取锁, 未获取到会阻塞程序, 知道获取到才会继续往下执行
# lock.acquire()
# 释放锁, 归还锁, 其它可以用
# lock.release()
# lock.acquire() 和 lock.release()必须成对出现. 否则就有可能造成死锁
# 为了规避死锁问题, 使用上下文管理器来加锁
# with lock:
# 这里写自己的代码
# ...
# 加锁是为了对锁内资源（变量）进行锁定,避免其他线程篡改已被锁定的资源,以达到我们预期的效果
def job1():
    global n, lock
    with lock:
        for i in range(10):
            n += 1
            print('job1: ', n)


def job2():
    global n, lock
    with lock:
        for i in range(10):
            n += 10
            print('job2: ', n)


# n = 0
# thread_5 = threading.Thread(target=job1)
# thread_6 = threading.Thread(target=job2)
# thread_5.start()
# thread_6.start()


# 可重入锁
def main():
    n = 0
    # 可重入锁
    # 在同一线程里，程序就当你是同一个人，这个锁就可以复用
    lock = threading.RLock()
    with lock:
        for i in range(10):
            n += 1
            with lock:
                print(n)


# thread_7 = threading.Thread(target=main)
# thread_7.start()

# 防止死锁的加锁机制
# =====================================【多线程的锁机制】=====================================


# =====================================【多线程的消息通信机制】=====================================
# 如何控制线程的触发执行 本质是消息通信机制起作用
# 通信方法有三种: threading.Event  threading.Condition  queue.Queue
# 关于 threading.Event 的使用
event = threading.Event()


# 重置 event 使得所有该 event 事件都处于待命状态
# event.clear()
# 等待接收 event 的指令, 决定是否阻塞程序执行
# event.wait()
# 发送 event 指令, 使所有设置该 event 时间的线程执行
# event.set()
# 例如
class MyThrend_1(Thread):
    def __init__(self, name, event):
        super(MyThrend_1, self).__init__()
        self.name = name
        self.event = event

    def run(self) -> None:
        print(
            'Thread: {} start at {}'.format(
                self.name, time.ctime(
                    time.time())))
        # 等待后才往下执行
        self.event.wait()
        print(
            'Thread: {} finish at {}'.format(
                self.name, time.ctime(
                    time.time())))


# threads = list()
# # 定义五个线程
# [threads.append(MyThrend_1(str(i), event)) for i in range(5)]
# # 重置 event 使得 event.wait 起到阻塞作用
# event.clear()
# # 启动所有线程
# [thread.start() for thread in threads]
# print('等待5秒...')
# time.sleep(5)
# print('唤醒所有线程...')
# event.set()

# 关于 threading.Condition 的使用
condition = threading.Condition()


# 类似 Lock.acquire()
# condition.acquire()
# 类似 Lock.release
# condition.release()
# 等待指定触发, 同时会释放对锁的获取, 直到被 notify 才重新占有锁
# condition.wait()
# 发送指令, 触发执行
# condition.notify()
class Hider(Thread):
    def __init__(self, condition, name):
        super(Hider, self).__init__()
        self.condition = condition
        self.name = name

    def run(self) -> None:
        # 确保先运行 Seeker 中得方法
        print('----------0------------')
        time.sleep(1)
        print('----------2------------')
        self.condition.acquire()

        print(self.name + ': 我已经把眼睛蒙上了')
        self.condition.notify()
        self.condition.wait()
        print('----------4------------')
        print(self.name + ': 我已经找到你了哦')
        self.condition.notify()
        print('----------5------------')

        self.condition.release()
        print(self.name + ': 我赢了')
        print('----------6------------')


class Seeker(Thread):
    def __init__(self, condition, name):
        super(Seeker, self).__init__()
        self.condition = condition
        self.name = name

    def run(self) -> None:
        print('----------1------------')
        self.condition.acquire()
        self.condition.wait()
        print('----------3------------')
        print(self.name + ': 我已经藏好了')
        self.condition.notify()
        self.condition.wait()
        print('----------7------------')
        self.condition.release()
        print(self.name + ': 被你找到了')
        print('----------8------------')


# seeker = Seeker(condition, 'seeker')
# hider = Hider(condition, 'hider')
# hider.start()
# seeker.start()
# hider: 我已经把眼睛蒙上了
# seeker: 我已经藏好了
# hider: 我已经找到你了哦
# hider: 我赢了
# seeker: 被你找到了

# 关于 Queue队列 的使用

# maxsize 默认 0 不受限
# 如果大于 0 消息又达到限制, q.put() 也将阻塞
q = Queue(maxsize=0)


# 默认阻塞程序, 等待队列消息, 可设置超时时间
# q.get(block=True, timeout=None)
# 发送信息, 默认会阻塞程序至队列中又空闲位置放入数据
# q.put(item, block=True, timeout=None)
# 等待所有的消息都被消费完
# q.join()
# 通知队列任务处理已经完成, 当所有任务都处理完成时, join() 阻塞会被解除
# q.task_done()
# 查询当前队列的消息个数
# q.qsize()
# 队列消息是否被消费完
# q.empty()
# 检测队列消息是否已满
# q.full()
class Student:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('{}: 到!'.format(self.name))


class Teacher:
    def __init__(self, queue):
        self.quque = queue

    def call(self, student):
        if student == 'exit':
            print('点名结束, 开始上课...')
        else:
            print('老师: {} 来了没'.format(student))
        self.quque.put(student)


class CallManager(Thread):
    def __init__(self, queue):
        super(CallManager, self).__init__()
        self.students = dict()
        self.quque = queue

    def put(self, student):
        self.students.setdefault(student.name, student)

    def run(self) -> None:
        while True:
            # 阻塞程序, 时刻监听老师, 接收消息, 一直在等待, 可以设置超时时间, 在超时时间内未获取到, 抛错
            student = self.quque.get()
            if student == 'exit':
                break
            elif student in self.students:
                self.students[student].speak()
            else:
                print('老师, 没有 {} 这个人'.format(student))


teacher = Teacher(q)
student_1 = Student('muzili')
student_2 = Student('xiaoli')
# cm = CallManager(q)
# cm.put(student_1)
# cm.put(student_2)
# cm.start()
#
# print('开始点名...')
# teacher.call('xiaoli')
# time.sleep(1)
# teacher.call('muzili')
# time.sleep(1)
# teacher.call('mr.li')
# time.sleep(1)
# teacher.call('exit')

# queue.LifoQueue: 后进先出队列
# queue.Queue: 先进先出队列
# queue.PriorityQueue: 优先级高的先出
# =====================================【多线程的消息通信机制】=====================================


# =====================================【多线程的信息隔离】=====================================
# 什么是信息隔离:
# 比如: 有两个线程,线程A里的变量,和线程B里的变量值不能共享.这就是信息隔离
# 定义一个 local 实例

local_data = threading.local()
# 在主线中, 存入 name 这个变量
local_data.name = 'local_data'


class MyThread_2(Thread):
    def run(self) -> None:
        print('赋值前子线程: ', currentThread(), local_data.__dict__)
        # 在子线程中存入 name 这个变量
        local_data.name = self.getName()
        print('赋值后子线程: ', currentThread(), local_data.__dict__)


# if __name__ == '__main__':
#     print('开始前主线程: ', local_data.__dict__)
#     thread_8 = MyThread_2()
#     thread_8.start()
#     thread_8.join()
#
#     thread_9 = MyThread_2()
#     thread_9.start()
#     thread_9.join()
#     print('结束后主线程: ', local_data.__dict__)
#     # 开始前主线程: {'name': 'local_data'}
#     # 赋值前子线程: < MyThread_2(Thread - 3, started 17132) > {}
#     # 赋值后子线程: < MyThread_2(Thread - 3, started 17132) > {'name': 'Thread-3'}
#     # 赋值前子线程: < MyThread_2(Thread - 4, started 10864) > {}
#     # 赋值后子线程: < MyThread_2(Thread - 4, started 10864) > {'name': 'Thread-4'}
#     # 结束后主线程: {'name': 'local_data'}
#     # 总结:
#     # 主线程中的变量, 不会因为是全局变量而被子线程获取到
#     # 主线程也不能获取到子线程中的变量
#     # 子线程与子线程之间不会互相访问

# =====================================【多线程的信息隔离】=====================================


# =====================================【线程池创建的几种方法】=====================================


def target():
    for i in range(5):
        print('running thread-{} : {}'.format(threading.get_ident(), i))
        time.sleep(1)


# 使用 ThreadPoolExecutor 类来创建线程池
# pool = ThreadPoolExecutor(5)
#
# for i in range(10):
#     # 往线程池上塞任务
#     pool.submit(target)

# 使用上下午管理器创建线程池  一次性同时运行 5 个线程
# with ThreadPoolExecutor(5) as pool:
#     for i in range(10):
#         pool.submit(target)

# 自定义线程池

# =====================================【线程池创建的几种方法】=====================================

# =====================================【yield 开始入门协程】=====================
# 协程特点
# 1. 协程是在单线程里面实现任务的切换的
# 2. 利用同步的方式去实现异步
# 3. 不再需要锁, 提高了并发性能


# yield from的用法详解
astr = 'ABC'
alist = [1, 2, 3]
adict = {'name': 'muzili', 'age': 18}
# 生成器
agen = (i for i in range(4, 8))


def gen(*args):
    for item in args:
        for i in item:
            yield i


# new_list = gen(astr, alist, adict, agen)
# print(list(new_list))


def gen1(*args):
    for item in args:
        # yield from 后面可加上 可迭代对象
        # 把可迭代对象里的每个元素一个一个的yield出来,对比yield来说代码更加简洁,结构更加清晰
        yield from item


# new_list = gen1(astr, alist, adict, agen)
# print(list(new_list))


# 复杂应用: 生成器的嵌套
# 调用方: 调用委派生成器的客户端 (调用方) 代码
# 委托生成器: 包含yield from表达式的生成器函数
# 子生成器: yield from后面加的生成器函数
def average_gen():
    # 子生成器
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total / count
    return total, count, average


def proxy_gen():
    # 委托生成器
    # 作用:
    # 在调用方与生成器之间建立一个双向通道
    # 调用方可以通过send() 直接给子生成器, 子生成器 yield 的值直接返回给调用方
    while True:
        total, count, average = yield from average_gen()
        print(
            '计算完毕\n总传入: {} 个数值, 总和: {}, 平均数: {}'.format(
                count, total, average))


def main_1():
    # 调用方
    calc_average = proxy_gen()
    next(calc_average)  # 预激协程
    print(calc_average.send(10))
    print(calc_average.send(20))
    print(calc_average.send(30))
    calc_average.send(None)  # 结束协程
    # 如果此处再调用 calc_average.send(10), 由于上一协程已经结束,将重开一协程


# main_1()
# =====================================【yield 开始入门协程】=====================


# =====================================【初识异步IO框架: asyncio】================
# 只要在函数前面加上 async 关键字, 这个函数对象就是一个协程


async def hello(name):
    print('hello ', name)


coroutine = hello('muzili')


# print(isinstance(coroutine, Coroutine))

# 将一个生成器直接变成协程使用
@asyncio.coroutine
def hello_1():
    yield from asyncio.sleep(1)


coroutine_1 = hello_1()


# print(isinstance(coroutine_1, Coroutine))
# print(isinstance(coroutine_1, Generator))


# event_loop: 事件循环 程序开启一个无限循环, 程序员把一些函数注册到事件循环上, 当满足事件发生的时候, 调用相应的协程函数
# coroutine: 协程对象 指使用async 关键字定义函数, 它调用不会立刻执行函数, 而是返回一个协程对象, 协程对象需要注册到事件循环, 由事件循环调用
# future: 对象 代表将来执行或没有执行任务的结果. 和task 没有本质区别
# task: 任务 一个协程对象就是一个原生可以挂起的函数, 任务则是对协程进一步封装, 其中包括任务的各种状态
#       task 对象是 future 的子类, 它将coroutine 和future 联系在一起, 将coroutine 封装成一个 future 对象
# async/await: async 定义一个协程, await 用于挂起阻塞的异步调用接口, 其作用类似 yield

# ==========================协程完整工作流程==========================
# 定义/创建协程对象
# 将协程转为 task 任务
# 定义事件循环对象容器
# 将task 任务扔进事件循环对象中触发
# ==========================协程完整工作流程==========================
async def hello_2(name):
    print('hello ', name)


# # 定义协程对象
# coroutine_2 = hello_2('muzili')
# # 定义事件循环对象容器
# loop = asyncio.get_event_loop()
# # 将协程转为task 任务
# task = loop.create_task(coroutine_2)
# # 将task 任务扔进事件循环对象中炳触发
# loop.run_until_complete(task)

# await与yield对比
# 不能在生成器中使用await
# 不能在async 定义的协程中使用yield from
# yield from 后面可接 可迭代对象 也可以接 future对象/协程对象
# await 后面必须接 future对象/协程对象

# asynico.sleep(n) 模拟IO阻塞, 返回一个协程对象
func = asyncio.sleep(2)


# print(isinstance(func, asyncio.Future))  # False
# print(isinstance(func, Coroutine))  # True


async def hello_3(name):
    await asyncio.sleep(2)
    print('hello ', name)


coroutine_3 = hello_3('muzili')

# 将协程转为 task 对象
task = asyncio.ensure_future(coroutine_3)


# loop_3 = asyncio.get_event_loop()
# loop_3.run_until_complete(task)

# print(isinstance(task, asyncio.Future))  # True


# 绑定回调函数  ->  给协程添加回调函数
# 异步IO的实现原理,就是在IO高的地方挂起,等IO结束后,再继续执行
# 回调实现有两种  1.利用的同步编程实现的回调


async def _sleep(x):
    print('stop')
    time.sleep(x)
    print('end')
    return 'stop {} second'.format(x)


coroutine_4 = _sleep(2)
loop_1 = asyncio.get_event_loop()


# task_1 = asyncio.ensure_future(coroutine_4)
# loop_1.run_until_complete(task_1)

# print('result return: {}'.format(task_1.result()))


# 回调实现有两种  2.通过asyncio自带的添加回调函数功能来实现
def callback(future):
    print('this is callback, the is result return: {}'.format(future.result()))


coroutine_5 = _sleep(2)
loop_2 = asyncio.get_event_loop()
task_2 = asyncio.ensure_future(coroutine_5)


# 添加回调函数
# task_2.add_done_callback(callback)
# loop_2.run_until_complete(task_2)


# 协程中的并发
async def do_some_work(x):
    print('waiting: ', x)
    await asyncio.sleep(x)
    return 'done after {}s'.format(x)


# 协程对象
coroutine_6 = do_some_work(1)
coroutine_7 = do_some_work(2)
coroutine_8 = do_some_work(4)
# 将协程转成task 并组成list
tasks = [
    asyncio.ensure_future(coroutine_6),
    asyncio.ensure_future(coroutine_7),
    asyncio.ensure_future(coroutine_8)
]

loops = asyncio.get_event_loop()


# 将协程注册到事件循环中  方法一: 使用asynci.wait()
# loops.run_until_complete(asyncio.wait(tasks))
# 方法二: 使用 asynic.gather()
# loops.run_until_complete(asyncio.gather(*tasks))
# for t in tasks:
#     print('test ret: ', t.result())


# 协程中的嵌套
async def main_2():
    # 创建三个协程对象
    coroutine_9 = do_some_work(1)
    coroutine_10 = do_some_work(2)
    coroutine_11 = do_some_work(4)

    # 将协程转为 task 并组成 list
    tasks_1 = [
        asyncio.ensure_future(coroutine_9),
        asyncio.ensure_future(coroutine_10),
        asyncio.ensure_future(coroutine_11)
    ]

    # 【attention】: await 一个 task 列表(协程)
    # dones: 表示已经完成的任务
    # pendings: 表示未完成的任务
    dones, pendings = await asyncio.wait(tasks_1)
    print('dones : ', dones)
    print('pendings : ', pendings)

    for t_1 in tasks_1:
        print('t_1 ret: ', t_1.result())

    # 方法二:  使用 asynic.gather()
    results = await asyncio.gather(*tasks_1)
    for result in results:
        print('result ret: ', result)


# loops_1 = asyncio.get_event_loop()
# 将封装好的协程函数丢进去 事件循环 对象容器中
# loops_1.run_until_complete(main_2())


# 协程中的状态
async def hello_4():
    print('running in the loop...')
    flag = 0
    while flag < 1000:
        with open('test.txt', 'a') as f:
            f.write('------')
        flag += 1
    print('stop the loop')


# if __name__ == '__main__':
#     coroutine = hello_4()
#     loop = asyncio.get_event_loop()
#     task = asyncio.create_task(coroutine)
#
#     # pending: 未执行状态
#     print(task)
#     try:
#         thread_3 = threading.Thread(target=loop.run_until_complete, args=(task,))
#         # thread_3.daemon = True
#         thread_3.start()
#
#         # running: 运行状态
#         time.sleep(1)
#         print(task)
#         thread_3.join()
#     except KeyboardInterrupt as e:
#         # 取消任务
#         task.cancel()
#         # cacelled: 取消任务
#         print(task)
#     finally:
#         print(task)
# 顺利执行的话,将会打印 Pending -> Pending：Runing -> Finished 的状态变化
# 执行后 立马按下 Ctrl+C,则会触发task取消,就会打印 Pending -> Cancelling -> Cancelling 的状态变化


# wait有控制功能
async def coro(tag):
    await asyncio.sleep(random.uniform(0.5, 5))


loop_3 = asyncio.get_event_loop()
tasks_3 = [coro(i) for i in range(1, 11)]


# [控制运行任务数]
# FIRST_COMPLETED: 运行第一个任务就完全返回
# FIRST_EXCEPTION: 产生第一个异常就完全返回
# ALL_COMPLETED: 所有任务完成返回(默认值)
# dones, pendings = loop_3.run_until_complete(
#     asyncio.wait(
#         tasks_3, return_when=asyncio.FIRST_COMPLETED
#     )
# )
# print('the frist finish task: ', len(dones))
#
# # 【控制时间】: 运行一秒后就返回
# dones2, pendings2 = loop_3.run_until_complete(
#     asyncio.wait(
#         pendings, timeout=1
#     )
# )
#
# print('the second finish task: ', len(dones2))
#
# dones3, pendings3 = loop_3.run_until_complete(
#     asyncio.wait(
#         pendings2
#     )
# )
#
# print('the three finish task: ', len(dones3))
# loop_3.close()


# 动态添加协程
def start_loop(loop):
    # 一个在后台永远运行的事件循环
    asyncio.set_event_loop(loop)
    loop.run_forever()


def do_sleep(x, queue, msg=''):
    time.sleep(x)
    queue.put(msg)


queue = Queue()
new_loop = asyncio.new_event_loop()


# 定义一个线程, 并传入一个事件循环对象
# thread_11 = Thread(target=start_loop, args=(new_loop,))
# thread_11.start()
#
# print(time.ctime())

# # 动态添加两个协程
# # 这种方法, 在主线程是同步的
# new_loop.call_soon_threadsafe(do_sleep, 6, queue, 'first')
# new_loop.call_soon_threadsafe(do_sleep, 3, queue, 'second')
#
# while True:
#     msg = queue.get()
#     print('{} 协程运行完...'.format(msg))
#     print(time.ctime())
#     # 运行完需要 9 秒

async def do_sleep_1(x, queue, msg=''):
    await asyncio.sleep(x)
    queue.put(msg)


# 定义一个线程, 并传入一个事件循环对象
thread_12 = Thread(target=start_loop, args=(new_loop,))
thread_12.start()

print(time.ctime())
# 动态添加两个协程
# 这种方法, 在主线程是异步的
asyncio.run_coroutine_threadsafe(do_sleep_1(6, queue, 'async first'), new_loop)
asyncio.run_coroutine_threadsafe(
    do_sleep_1(3, queue, 'async second'), new_loop)

while True:
    msg = queue.get()
    print('{} 协程运行完...'.format(msg))
    print(time.ctime())
    # 运行完需要 6 秒

# =====================================【初识异步IO框架: asyncio】================
