from django.urls import path
from . import views

urlpatterns = [
    path('crop/', views.crop_predict.as_view()),
    path('fertilizer/', views.fertilizer_predict.as_view()),
    path('disease/', views.disease_predict.as_view()),
    path('market/', views.market_stats.as_view()),
]