# coding=utf-8
# Time: 2024/8/11 15:17
# name: test
# author: wyp

class TestDes:
    def __get__(self, instance, owner):
        print('TestDes:__get__', instance, owner)
        return 'TestDes:__get__'

    def __set__(self, instance, value):
        print('TestDes:__set__', instance, value)
