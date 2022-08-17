from rest_framework import serializers
from crud.models import user

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'url', 'name', 'email', 'password']