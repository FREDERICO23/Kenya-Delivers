from django.urls import path
from .views import HomePageView
from . import views

urlpatterns = [
    #path('',HomePageView.as_view(), name='index'),
    path('',views.homepage, name='homee')
]
