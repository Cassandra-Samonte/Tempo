from django.shortcuts import render, redirect
from .seed_artist import Artists
from .models import Artist
from .main import *

def landing(request):
    return render(request, 'tempo_app/landing.html')

def artist(request):
    # Get artist object matching name
    artist = Artist.objects.get(name='Drake')
    
    # use main.py functions(funtions to use spotify api)
    token = get_token()
    result = search_for_artist(token, artist.name)

    artist_id = result["id"]

    songs = get_songs_by_artist(token, artist_id)
    song_list = []
    for song in songs:
        song_list.append(song['name'])

    return render(request, 'tempo_app/artist.html',{
        'artist':artist.name,
        'songs': song_list
    })

def artist_api(request):
    return render(request, 'tempo_app/artist_api.html')

def seed_artists(request):
    for artist in Artists:
        c = Artist(name=artist['name'])
        c.save()
        

    return redirect('landing')