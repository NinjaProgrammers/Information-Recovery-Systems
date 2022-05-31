from django.urls import path

from .views import HomePageView, ModelView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("model/<str:model>", ModelView, name="model"),
]
