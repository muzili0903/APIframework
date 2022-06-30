import os

import allure
import pytest

from com.util.getFileDirs import HISTORY


@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
@allure.story()
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False

# days(int)	间隔几天
# hours(int)	间隔几小时
# minutes(int)	间隔几分钟
# seconds(int)	间隔多少秒
# start_date(datetime or str)	开始日期
# end_date(datetime or str)	结束日期
def scheduler_params(con):
    params = list()
    weeks = eval(con.get_config('scheduler', 'weeks'))
    days = eval(con.get_config('scheduler', 'days'))
    hours = eval(con.get_config('scheduler', 'hours'))
    minutes = eval(con.get_config('scheduler', 'minutes'))
    seconds = eval(con.get_config('scheduler', 'seconds'))
    start_date = eval(con.get_config('scheduler', 'start_date'))
    end_date = eval(con.get_config('scheduler', 'end_date'))
    if weeks is not None:
        params.append('weeks={}'.format(weeks))
    if days is not None:
        params.append('days={}'.format(days))
    if hours is not None:
        params.append('hours={}'.format(hours))
    if minutes is not None:
        params.append('minutes={}'.format(minutes))
    if seconds is not None:
        params.append('seconds={}'.format(seconds))
    if start_date is not None:
        params.append('start_date={}'.format(start_date))
    if end_date is not None:
        params.append('start_date={}'.format(end_date))
    return params


@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True


if __name__ == "__main__":
    pytest.main(['-vs', './test.py', '--clean-alluredir', '--alluredir', HISTORY + '/xml',
                 '--disable-warnings'])
    cmd = 'allure generate --clean %s -o %s ' % (HISTORY + '/xml', HISTORY + '/html')
    os.system(cmd)
