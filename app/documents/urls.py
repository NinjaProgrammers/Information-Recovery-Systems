from django.urls import path

from .views import HomePageView, SearchResultsView

urlpatterns = [
    path("", SearchResultsView, name="search_results"),
    #path("", HomePageView.as_view(), name="home"),
]
