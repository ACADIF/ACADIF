from django.urls import path
from MyAuth import views

urlpatterns = [
    path('signin/', views.sign_in, name='signin'),
]