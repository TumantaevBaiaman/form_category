from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . import models


class SerializerCreateForm(serializers.Serializer):

    class Meta:
        model = models.MyForm
        fields = ["name"]


class SerializerCreateField(serializers.Serializer):

    class Meta:
        models = models.Fields
        filter = ["email", "phone", "text", "date"]
        extra_kwargs = {'form': {'required': False}}

