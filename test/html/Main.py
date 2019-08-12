#!/usr/bin/python
# -*- coding: UTF-8 -*-


# from Router import router
# from Config import start
#
#
# start(router)

import json


class Student(object):
    def __init__(self, name, age, score, reward):
        self.name = name
        self.age = age
        self.score = score
        self.reward = reward

eval('stu=Student("Bob", 20, 88, ["三好学生", "优秀团干", "最佳辩手"])')

# stu = Student('Bob', 20, 88, ["三好学生", "优秀团干", "最佳辩手"])
# print json.dumps(obj=stu.__dict__, ensure_ascii=False)
#
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'],d['reward'])
#
# json_str = '{"name": "Bob", "age": 20, "score": 88, "reward": ["三好学生", "优秀团干", "最佳辩手"]}'
# student = json.loads(json_str,object_hook=dict2student)
# print(type(student))
# print(student.name)
