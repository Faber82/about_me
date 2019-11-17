from django.urls import path
from . import views

urlpatterns = [
    path('', views.rep_list, name='About_me'),
    path("<int:pk>/", views.rep_detail, name="repository_detail"),
    path('experience/', views.experience_view, name='experience'),
]
