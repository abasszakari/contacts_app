from django.urls import path
from . import views

app_name = 'contacts_app'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('form/', views.contact_form, name='contact_add'),
    path('form/<int:id>', views.contact_form, name='contact_update'),
    path('delete/<int:id>', views.contact_delete, name='contact_delete')
]