import factory.django

from user.models import User
from ad.models import Ad


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "123test"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Temp-name for test"
    price = 100
    description = ""
    author = factory.SubFactory(UserFactory)
