from django.contrib import admin
from django.urls import path
from sales.views import listorders, listorders2, listcustomers, listorders3

urlpatterns = [

    path('orders/', listorders),
    path('orders2/', listorders2),
    path('orders3/', listorders3),
    path('customers_list/', listcustomers),
]
