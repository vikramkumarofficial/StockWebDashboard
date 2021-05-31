from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import re


class RegisterSerializer(serializers.ModelSerializer):
    mobile_number = serializers.IntegerField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password',
                  'mobile_number', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        username = attrs['username']
        user = User.objects.filter(username=username)
        if user:
            raise serializers.ValidationError(
                "That user is already taken , please select another ")
        elif not re.search(r'^\w+$', username):
            raise serializers.ValidationError(
                "Username can only contain"
                "alphanumeric characters and the underscore.")
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            mobile_number=validated_data['mobile_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
