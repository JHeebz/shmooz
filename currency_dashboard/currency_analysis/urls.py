from django.urls import path
from . import views

urlpatterns = [
    path('rand-vs-dollar/', views.rand_vs_dollar, name='rand_vs_dollar'),
    path('dollar-to-aud/', views.dollar_to_aud, name='dollar_to_aud'),
]
