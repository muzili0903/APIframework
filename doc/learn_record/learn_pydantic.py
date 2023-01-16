# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2023/1/5 14:37
@file    :learn_pydantic.py
"""
from typing import Text, List, Optional, Any, Union
import re
from pydantic import BaseModel, validator


# pydantic 是一种常用于数据接口 schema 定义与检查的库

# 基本的schema定义方法
class Person(BaseModel):
    name: Text
    age: List
    # 可选类型 不传默认为空
    weigth: Optional[Text]
    # 联合类型 不传默认为空
    heigth: Union[None, Any, Text]


# 基本的schema实例化方法
# 1、直接传值
p = Person(name='muzili', age=[1, 2], weigth=30, heigth=[160])
print(p.json())
print(p.dict())
print(p.name)
print(p.age)
# 2、通过字段传入
d = {'name': 'muzili', 'age': [1, 2]}
p = Person(**d)
print(p.name)
print(p.json())
# 3、通过其它实例化对象传入
pp = Person.copy(p)
print(pp.json())
# 传入值错误会抛错
# Person(person='xiaoli')
# 如果传入值多于定义值时，BaseModel也会自动对其进行过滤。pydantic在数据传输时会直接进行数据类型转换
# weigth=30 自动转化为 weigth="30"
p = Person(name='muzili', age=[1, 2], weigth=30, heigth=['160'], sex=1)

from enum import Enum
from typing import List, Union
from datetime import date
from pydantic import BaseModel


# 多级schema定义样例
class Gender(str, Enum):
    man = "man"
    women = "women"


class Person(BaseModel):
    name: str
    gender: Gender


class Department(BaseModel):
    name: str
    lead: Person
    cast: List[Person]


class Group(BaseModel):
    owner: Person
    member_list: List[Person] = []


class Company(BaseModel):
    name: str
    owner: Union[Person, Group]
    regtime: date
    department_list: List[Department] = []

    @validator('name')
    def name_rule(cls, name):
        def is_valid(name):
            if len(name) < 6 or len(name) > 20:
                return False
            return True

        if not is_valid(name):
            raise ValueError("name is invalid")

        return name


sales_department = {
    "name": "sales",
    "lead": {"name": "Sarah", "gender": "women"},
    "cast": [
        {"name": "Sarah", "gender": "women"},
        {"name": "Bob", "gender": "man"},
        {"name": "Mary", "gender": "women"}
    ]
}

research_department = {
    "name": "research",
    "lead": {"name": "Allen", "gender": "man"},
    "cast": [
        {"name": "Jane", "gender": "women"},
        {"name": "Tim", "gender": "man"}
    ]
}

company = {
    "name": "Fantasy",
    "owner": {'owner': {"name": "Victor", "gender": "man"}, 'member_list': [{"name": "Victor", "gender": "man"}, {"name": "Victor", "gender": "man"}]},
    "regtime": "2020-7-23",
    "department_list": [
        sales_department,
        research_department
    ]
}

company = Company(**company)
print(company.json())


class Password(BaseModel):
    password: str

    @validator("password")
    def password_rule(cls, password):
        def is_valid(password):
            if len(password) < 6 or len(password) > 20:
                return False
            if not re.search("[a-z]", password):
                return False
            if not re.search("[A-Z]", password):
                return False
            if not re.search("\d", password):
                return False
            return True

        if not is_valid(password):
            raise ValueError("password is invalid")

        return password


p1 = Password(password='1232aA321')
print(p1.json())
