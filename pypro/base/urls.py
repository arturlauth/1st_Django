from django.urls import path

from pypro.base.views import home

<<<<<<< HEAD
app_name = 'base'
=======
app_name='base'
>>>>>>> origin/master
urlpatterns = [
    path('', home, name='home'),
]
