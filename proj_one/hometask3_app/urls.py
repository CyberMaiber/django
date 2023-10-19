from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('orders/<int:client_id>/<int:days_count>', views.orders_of_client,name='orders_of_client'),
]