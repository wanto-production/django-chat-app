from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/', views.post, name='post'),
    path('login/', views.loginPage,name='login'),
    path('register/', views.register,name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('post/new/', views.create_post,name='create_post'),
    path('post/<str:post_title>/delete/', views.delete_post, name='delete_post'),
    path('post/<str:post_title>/edit/', views.update_post,name='update_post')
]