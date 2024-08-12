# -*- coding: utf-8 -*-

from rest_framework import serializers

from django.contrib.auth import get_user_model
from rest_framework import serializers
from app0 import models

USER_MODEL = get_user_model()


class UpdateUserInfoRequestSerializer(serializers.Serializer):
    new_username = serializers.CharField(label="新用户名", max_length=12, min_length=6)


class UpdateUserInfoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ["id", "username", "last_login"]


class StuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"


