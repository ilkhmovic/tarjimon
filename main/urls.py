from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarjimon, name='tarjimon'),
    path('api/translate/', views.translate_api, name='translate_api'),
    path('history/', views.translation_history, name='history'),
]