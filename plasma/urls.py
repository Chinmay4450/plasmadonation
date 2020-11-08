from django.urls import path, re_path
from plasma import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('requestt', views.requestt, name='requestt'),

]
