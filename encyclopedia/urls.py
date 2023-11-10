from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entries, name="entries"),
    path("search/", views.search, name="search"),
    path("search_results/<str:query>", views.search_results, name="search_results"),
]
