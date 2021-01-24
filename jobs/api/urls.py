from django.urls import path
from jobs.api import views

urlpatterns = [
    path('jobs/', views.ListView.as_view(), name='list'),
    path('jobs/<int:pk>/', views.DetailView.as_view(),name='detail'),
]
