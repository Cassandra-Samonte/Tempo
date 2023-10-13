from django.shortcuts import render


def landing(request):
    return render(request, 'tempo_app/landing.html')

def artist(request):
    return render(request, 'tempo_app/artist.html')

def artist_api(request):
    return render(request, 'tempo_app/artist_api.html')