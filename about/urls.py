from django.urls import path
from .views import BlogListView


urlpatterns = [
    path("about/", BlogListView.as_view(), name="about"),
    ]