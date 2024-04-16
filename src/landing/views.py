from django.shortcuts import render


def index_view(request):
    return render(request, "index.html")


def portfolio_view(request):
    return render(request, "portfolio.html")


def about_view(request):
    return render(request, "about.html")


def contacts_view(request):
    return render(request, "contacts.html")
