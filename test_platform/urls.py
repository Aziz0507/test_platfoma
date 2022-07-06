from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('buttons/<int:pk>', views.buttons, name = 'buttons'),
    path('test/<int:pk>', views.test, name = 'test'),
]
