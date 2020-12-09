from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('posts/', views.PostView.as_view(), name='posts'),
  path('add/', views.AddPost.as_view(), name='add'),
  path('<slug:slug>/', views.SinglePost.as_view(), name='detail'),
  path('edit/<int:pk>/', views.EditView.as_view(), name="edit"),
  path('delete/<int:pk>/', views.DeletePost.as_view(), name="delete"),
]