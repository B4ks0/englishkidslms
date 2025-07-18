from django.shortcuts import render
from django.http import Http404

def custom_404(request, exception=None):
    """
    Custom 404 error handler view
    """
    return render(request, '404.html', status=404)

def custom_500(request, exception=None):
    """
    Custom 500 error handler view
    """
    return render(request, '500.html', status=500) 