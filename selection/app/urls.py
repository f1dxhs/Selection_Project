from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name = 'search'),
    path('results/', views.search, name = 'results'),
    path('no_results/', views.search, name='no_results'),
    path('alldata/', views.show_all_data, name = 'alldata'),
]
