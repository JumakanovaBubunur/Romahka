from django.urls import path
from .views import (HomePageView, AboutPageView, ConditionPageView, RegistrationPageView, RegimePageView)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("condition/", ConditionPageView.as_view(), name="condition"),
    path("registration", RegistrationPageView.as_view(), name="registration"),
    path("regime", RegimePageView.as_view(), name="regime"),
]