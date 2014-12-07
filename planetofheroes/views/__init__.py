from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required


def portada(request):
    return render(request, 'planetofheroes/portada.html', {})