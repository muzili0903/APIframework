# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2022/6/14 9:38
@file    :conftest.py
"""
import pytest
import requests


@pytest.fixture(scope='session', autouse=False)
def login_manage():
    """
    登陆
    :return:
    """
    request = requests.session()
    admin = {
        'header': {
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        'url': r'https://efssit.midea.com/admin/'
    }
    result = request.get(url=admin.get('url'), headers=admin.get('header'), verify=False)

    login = {
        'url': 'https://signinuat.midea.com/login?service=https://efssit.midea.com/admin/',
        'header': {'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded'},
        'data': {'username': 'shirui4',
                 'password': 'c1VQySCorZcSqn1WD+JnJg==',
                 'execution': 'e1s1',
                 '_eventId': 'submit',
                 'geolocation': ''}
    }
    request.post(url=login.get('url'), data=login.get('data'), headers=login.get('header'),
                 cookies=result.cookies)
    return request
