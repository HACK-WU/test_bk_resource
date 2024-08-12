# -*- coding: utf-8 -*-

from bk_resource.viewsets import ResourceViewSet, ResourceRoute
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return Response("hello world")


class App0ViewSet(ResourceViewSet):
    resource_routes = []


from bk_resource import resource
from bk_resource.viewsets import ResourceRoute, ResourceViewSet
from app0 import resources


# 声明 ViewSet，其中，ViewSet前方的内容会成为 url 的一部分
class UserViewSet(ResourceViewSet):
    # 声明所有方法
    # Resource 会自动查找所有的子类并添加到 resource 中
    # 映射关系为 underscore_to_camel; 即 UpdateUserInfo => update_user_info
    resource_routes = [
        # 在这一条路由中，example.app0 为 APP 名，update_user_info 为 app0 下 resources.py 文件中的 UpdateUserInfoResource 对象
        # endpoint 不填写时默认为空，映射为根路由
        ResourceRoute("POST", resource.app0.update_people_info, endpoint="info/"),
        # # 我们也可以使用常规的方式进行声明，但不推荐
        # ResourceRoute("POST", UpdatePeopleInfoResource),
        # # 如果我们涉及到了 RestFul 标准的更新、删除类型，则可以使用 pk_field 声明，会自动将 pk 添加到 validated_request_data 中
        # ResourceRoute("PUT", UpdatePeopleInfoResource, pk_field="user_id"),
        ResourceRoute("GET", resources.UpdatePeopleInfoResource),
    ]


# 类名即路由
class StuViewSet(ResourceViewSet):
    resource_routes = [
        # ResourceRoute("GET", resource.app0.stu_list),
        ResourceRoute("GET", resources.StuListResource),
        ResourceRoute("POST", resources.StuCreateResource)
    ]


