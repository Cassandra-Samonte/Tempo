from django.shortcuts import render


def landing(request):
    return render(request, 'tempo_app/landing.html')