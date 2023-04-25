from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_drive, name = 'search_drive'),
    path('results/', views.search_drive, name = 'results_drive'),
    path('no_results/', views.search_drive, name='no_results_drive'),
    path('alldata/', views.show_all_data, name = 'alldata'),
]
