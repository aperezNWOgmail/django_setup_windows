from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path('getAllLogs', views.getAllLogs, name='getAllLogs'),
    path('getAllPersons', views.getAllPersons, name='getAllPersons'),
    path('getAllContactForms', views.getAllContactForms, name='getAllContactForms'),
    path('health/',  views.health_check, name='health_check'),  # Optional
    path('getPythonVersion'   , views.getPythonVersion,   name='getPythonVersion'),
    path('ping'               , views.ping,               name='ping'),
]