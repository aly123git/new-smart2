from django.urls import path
from . import views
app_name= 'home'

urlpatterns = [
    path('', views.home_en, name=''),
    path('certificates_en/', views.certificates_en, name='certificates_en'),

    path('home_ar/', views.home_ar, name='home_ar'),
    path('certificates_ar/', views.certificates_ar, name='certificates_ar'),

]
