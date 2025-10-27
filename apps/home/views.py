from django.shortcuts import render


def home(request):
    # Render the template "home.html" which extends base.html
    return render(request, "home.html")
