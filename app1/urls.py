from django.urls import path
from .import views
from django.contrib.auth import views as authviews

urlpatterns=[
    path('', views.front_page, name ='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('logout/', authviews.LogoutView.as_view(), name='logout'),
    path('login/', authviews.LoginView.as_view(template_name ='app1/login.html'), name ='login')
]
