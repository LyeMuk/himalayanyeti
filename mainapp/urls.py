from mainapp import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('donation', views.donation, name='donation'),
    path('help', views.help, name='help'),

]
