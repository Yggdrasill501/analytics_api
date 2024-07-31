from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.get_report, name='get_report'),
    path('sessions_by_country/', views.sessions_by_country, name='sessions_by_country'),
]
