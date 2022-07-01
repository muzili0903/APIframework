# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/5/18 9:01
@file    :APImain.py
"""

if __name__ == "__main__":
    from com.util.getConfig import Config
    from com.core.scheduler import scheduler_py
    from com.core.APIrun import run

    # from com.util import logOperation
    # from com.util.getFileDirs import LOGS

    # logOperation.MyLogs(LOGS)
    con = Config()
    # if eval(con.get_config('scheduler', 'is_scheduler').capitalize()):
    if con.get_config_bool('scheduler', 'is_scheduler'):
        scheduler_py(con)
    else:
        run()
