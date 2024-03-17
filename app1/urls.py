from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.home),
    path('index/', views.emp),
 path('admin/', admin.site.urls),
]