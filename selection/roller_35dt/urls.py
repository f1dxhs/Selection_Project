from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_roller, name = 'search_roller'),
    path('results/', views.search_roller, name = 'search_roller'),
    path('no_results/', views.search_roller, name='search_roller'),
]
