from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_alter, name = 'search_alter'),
    path('results/', views.search_alter, name = 'results_alter'),
    path('no_results/', views.search_alter, name='no_results_alter'),
    path('alldata/', views.show_all_data, name = 'alldata'),
]