from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.service_list, name='service_list'),
    path('reservation/', views.make_reservation, name='make_reservation'),
    path('payment/<int:reservation_id>/', views.payment, name='payment'),

]


