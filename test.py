import os

import allure
import pytest

from com.util.getFileDirs import HISTORY


@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
@allure.story()
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False


@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True


if __name__ == "__main__":
    pytest.main(['-vs', './test.py', '--clean-alluredir', '--alluredir', HISTORY + '/xml',
                 '--disable-warnings'])
    cmd = 'allure generate --clean %s -o %s ' % (HISTORY + '/xml', HISTORY + '/html')
    os.system(cmd)
