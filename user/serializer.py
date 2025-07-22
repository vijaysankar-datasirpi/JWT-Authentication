from rest_framework import serializers
from .models import users

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=users
        fields='__all__'
        extra_kwargs={
            'password':{'write_only':True}
        }