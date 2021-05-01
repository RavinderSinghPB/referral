from rest_framework import serializers
from .models import User, ReferCode


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'user_refer_code', 'used_refer_code')
        extra_kwargs = {'password': {'write_only': True, },
                        'user_refer_code': {'read_only': True, }}


class ReferCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReferCode
        fields = ('url', 'code', 'UserCreated')
