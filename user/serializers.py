from rest_framework import serializers

from user.models import Location, User


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)

        return user
