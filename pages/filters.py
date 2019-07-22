from django.contrib.auth.models import User
import django_filters
from pages.models import Post12

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Post12
        fields = ['animaltype','location']