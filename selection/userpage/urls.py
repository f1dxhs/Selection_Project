
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.choose_app, name='choose_app'),  # 选择 app 的页面
    # path('drive/',views.choose_app, name = 'redirect_drive'),
    # path('alter/', views.choose_app, name = 'redirect_alter'),
]

