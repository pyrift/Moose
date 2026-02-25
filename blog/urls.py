from django.urls import path
from .views import home_page,blog,about,contact
urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', blog, name='blog'),
    path('about/' ,about, name='about'),
    path('contact/',contact,name = 'contact')
]