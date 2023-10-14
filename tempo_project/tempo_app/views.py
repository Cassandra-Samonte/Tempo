from django.shortcuts import render
from .seed_artist import Artists

def landing(request):
    return render(request, 'tempo_app/landing.html')

def artist(request):
    return render(request, 'tempo_app/artist.html',{
        'artist':Artists[0],
    })

def artist_api(request):
    return render(request, 'tempo_app/artist_api.html')