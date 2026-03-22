from django.shortcuts import render
# Create your views here.
def landing_page(request):
    """
    Main landing page for Hamilton Foot Care
    """
    return render(request, 'core/landing.html', {})