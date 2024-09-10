from django.urls import path

from.views import signup
app_name = 'user'

urlpatterns = [
    path('signup/',signup,name='signup')
]
