# -*- coding: utf-8 -*-
"""
@Author  :ex_liyh33
@time    :2023/1/16 14:44
@file    :learn_comprehensions.py
"""
# 列表推导式
# new_list = [expression for_loop_expression if condition]
old_list = [0, 2, 3, 4, 5, 6]
new_list = [item for item in old_list if item % 2 == 0]
print(new_list)

# 字典推导式
# new_dict = {key_expression: value_expression for_loop_expression if
# condition}
old_student_score_info = {
    "Jack": {
        "chinese": 87,
        "math": 92,
        "english": 78
    },
    "Tom": {
        "chinese": 92,
        "math": 100,
        "english": 89
    }
}
new_student_score_info = {
    name: score for name,
    score in old_student_score_info.items() if score["math"] == 100}
print(new_student_score_info)

# 集合推导式
# new_set = {expression for_loop_expression if condition}
old_list_1 = [0, 0, 0, 0, 1, 2, 3]
new_set = {item for item in old_list_1}
print(new_set)

# 生成器推导式
# new_gen = (expression for_loop_expression if condition)
new_gen = (item for item in old_list if item % 2 == 0)
print(list(new_gen))

# 嵌套推导式
