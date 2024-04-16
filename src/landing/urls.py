from django.urls import path

from landing.views import index_view, portfolio_view, contacts_view, about_view

urlpatterns = [
    path("portfolio/", portfolio_view, name="portfolio"),
    path("contats/", contacts_view, name="contacts"),
    path("about/", about_view, name="about"),
    path("", index_view, name="index"),
]
