import django_filters
from .models import Review
from django_filters import CharFilter

class ReviewFilter(django_filters.FilterSet):

    game = CharFilter(field_name='game', lookup_expr='icontains')

    class Meta:
        model = Review
        fields = '__all__'