# -*- coding: utf-8 -*-

from bk_resource import Resource


class Demo(Resource):
    def perform_request(self, validated_request_data):
        return


#
# from bk_resource import Resource
# from blueapps.utils.request_provider import get_local_request
#
#
# class UpdateUserInfoResource(Resource):
#     """更新用户信息"""
#
#     def perform_request(self, validated_request_data):
#         # 获取 Request 对象
#         request = get_local_request()
#         # 获取 User 对象
#         user = request.user
#         # 获取新用户名并更新
#         new_username = validated_request_data.get("new_username")
#         if not new_username or len(new_username) != 12:
#             raise Exception("用户名不合法")
#         user.username = new_username
#         user.save()
#         # 响应信息
#         return {
#             "id": user.id,
#             "username": user.username,
#             "last_login": user.last_login,
#         }


from bk_resource import Resource
from blueapps.utils.request_provider import get_local_request
from app0.serializers import UpdateUserInfoRequestSerializer, UpdateUserInfoResponseSerializer

from django.contrib.auth import get_user_model


class UpdatePeopleInfoResource(Resource):
    """更新用户信息"""

    # 声明输入输出使用的 Serializer
    # 声明 RequestSerializer 后，所有请求都会自动校验，validated_request_data 可以直接获取校验完成的数据
    # RequestSerializer = UpdateUserInfoRequestSerializer
    # # 声明 ResponseSerializer 后，所有输出会自动校验
    ResponseSerializer = UpdateUserInfoResponseSerializer

    def perform_request(self, validated_request_data):
        # 获取 Request 对象
        request = get_local_request()
        # 获取 User 对象
        user = get_user_model().objects.first()
        # user = request.user
        # # 获取新用户名并更新
        # new_username = validated_request_data["new_username"]
        # print("new_username", new_username)
        # user.username = new_username
        # user.save()
        # 可以直接返回 User 对象，会按照 Serializer 自动格式化为对应的内容，当然，直接返回对应的字典格式也是可以的
        return user


from app0 import serializers
from app0 import models

from rest_framework import viewsets


class StuListResource(Resource):
    # RequestSerializer = serializers.StuSerializer

    # 当返回的数据是多个Model的对象时，many_response_data 需要设置为True
    many_response_data = True

    ResponseSerializer = serializers.StuSerializer

    def perform_request(self, validated_request_data):
        stu_list = models.Student.objects.all()
        print(stu_list)
        return stu_list


class StuCreateResource(Resource):
    # 不写则不进行校验
    RequestSerializer = serializers.StuSerializer

    ResponseSerializer = serializers.StuSerializer

    # serializer_class = serializers.StuSerializer

    def perform_request(self, validated_request_data):
        print(validated_request_data)

        stu = models.Student.objects.create(**validated_request_data)
        print(stu)

        return stu
