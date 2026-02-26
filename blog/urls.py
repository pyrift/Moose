from django.urls import path
from .views import home_page,blog_page,about_paggge,contact
urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', blog_page, name='blog'),
    path('about/' ,about_paggge, name='about'),
    path('contact/',contact,name = 'contact')
]