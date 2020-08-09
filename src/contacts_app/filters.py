import django_filters
from django_filters import DateFilter
from .models import *

class ContactFilter(django_filters.FilterSet):

	class Meta:
		model = Contact
		fields = '__all__'
		exclude = ['user', 'mobile', 'address']
