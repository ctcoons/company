from django.shortcuts import render


def home(request):
    """
    Render the homepage of the site.
    """
    context = {
        "title": "Home",
        "welcome_message": "Welcome to the Company homepage!"
    }
    return render(request, "home/home.html", context)
