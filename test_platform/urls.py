from django.urls import path, include, re_path
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('answer', views.user_test_views)



urlpatterns = [
    path('', views.main, name = 'main'),
    path('buttons/<int:pk>', views.buttons, name = 'buttons'),
    path('test-api/<int:pk>', views.TestApiViews.as_view(), name='test-api'),
    path('quiz/<int:pk>', views.Quiz, name = 'Quiz'),
    path('answer', views.Answer, name='Answer'),
    path('quiz/answer/', include(routers.urls), name ='rest-answer'),
    path('reg/', views.SignUpView, name = 'register'),
    path('djoser/', include('djoser.urls'), name = 'djoser'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
