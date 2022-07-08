from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('buttons/<int:pk>', views.buttons, name = 'buttons'),
    path('test-api/<int:pk>', views.TestApiViews.as_view(), name='test-api'),
]
