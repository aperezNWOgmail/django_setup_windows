from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("my_view", views.my_view, name="my_view"),
    path('getAllLogs', views.raw_sql_endpoint, name='raw_sql_endpoint'),
]
