from .views import *
from django.urls import path
from . import views
urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', blog_page, name='blog'),
    path('about/' ,about_page, name='about'),
    path('contact/<str:name>/', views.contact_page, name='contact'),
]