from django.urls import path

from .views import HomePageView, ModelView, RedirectView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("model/<str:modelname>/<str:dataset>", ModelView, name="model"),
    path("redirect", RedirectView, name="redirect"),
]
