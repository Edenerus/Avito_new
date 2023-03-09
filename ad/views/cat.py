from rest_framework.viewsets import ModelViewSet

from ad.models import Category
from ad.serializers import CategorySerializer


class CatViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
