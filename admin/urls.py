from django.urls import path
from admin import customer

urlpatterns = [
    path('customers/', customer.dipatcher)
]
