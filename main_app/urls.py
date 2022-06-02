from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('finchgallery/', views.FinchList.as_view(), name="finch_list"),
    path('finchgallery/new/', views.FinchCreate.as_view(), name= "finch_create"),
    path('finchgallery/<int:pk>/', views.FinchDetail.as_view(), name="finch_detail"),
    path('finchgallery/<int:pk>/update', views.FinchUpdate.as_view(), name="finch_update"),
    path('finchgallery/<int:pk>/delete', views.FinchDelete.as_view(), name="finch_delete")
]