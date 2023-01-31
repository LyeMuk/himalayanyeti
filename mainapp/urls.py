from mainapp import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('donation', views.donation, name='donation'),
    path('help', views.help, name='help'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('userlogout', views.userlogout, name='userlogout'),
    path('createuser', views.createuser, name='createuser'),
    path('addarticle', views.addarticle, name='addarticle'),

    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('government', views.government, name='government'),
    path('organisation', views.organisation, name='organisation'),
    path('institute', views.institute, name='institute'),
    path('individual', views.individual, name='individual'),
    path('csr', views.csr, name='csr'),
    path('getinvolved', views.getinvolved, name='getinvolved'),
    path('focusArea', views.focusArea, name='focusArea'),






    path('deletearticle/<int:num>', views.deletearticle, name="deletearticle"),
    path('viewarticle/<int:num>', views.viewarticle, name="viewarticle"),
    path('updatearticle/<int:pk>', views.updatearticle, name="updatearticle"),







]
