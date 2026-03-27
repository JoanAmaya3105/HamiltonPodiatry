from django.shortcuts import render
from django.templatetags.static import static
# Create your views here.
def landing_page(request):
    """
    Main landing page for Hamilton Foot Care
    """
    context = {
        'feet_image': static('images/feets.png'),
        'phone_number': '0224188248'
    }
    return render(request, 'core/landing.html', context)