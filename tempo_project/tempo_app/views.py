from django.shortcuts import render, redirect
from .seed_artist import Artists
from .models import Artist
from .main import *
from .main import get_token, search_for_artist


def home(request):
    return redirect('landing')
def landing(request):
    return render(request, 'tempo_app/landing.html')

def player(request):
    return render(request, 'tempo_app/player.html')

def merch(request):
    return render(request, 'tempo_app/merch.html')

def login(request):
    return render(request, 'tempo_app/login.html')

def artist(request, artist_id):
    # Get artist object matching name
    # artist = Artist.objects.get(name='Drake')
    artist = Artist.objects.get(id=artist_id)

    
    # use main.py functions(funtions to use spotify api)
    token = get_token()
    result = search_for_artist(token, artist.name)

    # Getting artist Id, necessary to get artist details
    artist_id = result["id"]

    # Getting artist top tracks using api
    songs = get_songs_by_artist(token, artist_id)

    # Putting all the song names into a list
    song_list = []
    for song in songs:
        song_list.append(song['name'])

    # Getting artist picture
    image_url = result["images"][0]["url"]
    print(image_url)

    return render(request, 'tempo_app/artist.html',{
        'artist': artist.name,
        'songs': song_list,
        'image_url': image_url,
    })

# def artist_api(request):
#     return render(request, 'tempo_app/artist_api.html')

def seed_artists(request):
    for artist in Artists:
        c = Artist(name=artist['name'])
        c.save()
        

    return redirect('landing')

# Artist Index
def artist_api(request):
    # Get list of all lists from database
    artists = Artist.objects.all()

    # Initialize an empty list to store data
    artist_data = []

    #  Get artist info from Spotify 
    for artist in artists:
        token = get_token()
        result = search_for_artist(token, artist.name)

        # Get artist name, image, and ID 
        if result:
            artist_name = result["name"]
            image_url = result["images"][0]["url"]
            print(image_url)
            spotify_id = result["id"]

        # Append artist data to the list 
        artist_data.append({
            "name": artist_name,
            "image_url": image_url,
            "spotify_id": spotify_id
        })
    return render(request, 'tempo_app/artist_api.html', {'artist_data': artist_data})
