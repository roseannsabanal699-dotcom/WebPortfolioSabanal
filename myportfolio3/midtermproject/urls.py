from django.urls import path
from midtermproject import views

urlpatterns = [
    path('midtermproject/', views.midtermproject, name='midtermproject'),
]
