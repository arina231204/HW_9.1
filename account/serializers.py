from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from datetime import date

from .models import Profile, User


def is_after_today(value):
    if value > date.today():
        raise serializers.ValidationError('Дата регистрации не должна быть раньше текущей даты')


class ProfileBuyerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],
        write_only=True
    )
    password = serializers.CharField(
        max_length=20,
        write_only=True
    )
    password_2 = serializers.CharField(
        max_length=20,
        write_only=True
    )

    class Meta:
        model = Profile
        exclude = ['user', 'is_sender',]

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile.objects.create(
            user=user,
            is_sender=False

        )
        return profile

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError("Пароли должны совпадать")
        return data

class ProfileSenderSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],
        write_only=True
    )
    password = serializers.CharField(
        max_length=20,
        write_only=True
    )
    password_2 = serializers.CharField(
        max_length=20,
        write_only=True
    )

    class Meta:
        model = Profile
        exclude = ['user', 'is_sender', ]

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile.objects.create(
            user=user,
            is_sender=True

        )
        return profile

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError("Пароли должны совпадать")
        return data