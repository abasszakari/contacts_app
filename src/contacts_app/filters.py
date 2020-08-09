import django_filters
from django_filters import CharFilter
from .models import *

class ContactFilter(django_filters.FilterSet):
	fullname = CharFilter(field_name='fullname', lookup_expr='icontains', label ='Full Name')
	organization = CharFilter(field_name='organization', lookup_expr='icontains', label ='Organization')
	class Meta:
		model = Contact
		fields = ['fullname', 'organization']
		
