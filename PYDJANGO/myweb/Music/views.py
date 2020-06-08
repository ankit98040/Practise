from django.shortcuts import render
#from django import http
from django.http import HttpResponse as hr
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login, authenticate, logout
from .forms import *


#def Home(request):
    #data = render_to_string("index.html")
    #return http.HttpResponse("<h1>hello guys</h1>")
    #Dict = {"Name": ["subhashri","sanjukta", "prapty"], "Age" :[27], "url": ["http://127.0.0.1:8000/jetix"]}
    #return hr(data, Dict)
    #return render(request, "index.html", Dict)
    #return render(request, "index.html")

def Home(request):
    name = ['ankit', 'Anubhav', 'Deep']
    url = ['https://www.facebook.com', 'https://google.com', 'https://linkedin.com']
    data = zip(name, url)
    Dict = {"names":data}
    return render(request, "index.html", Dict)

def Home2(request):
    nam = ["ankit", "amit","rohit", "sandeep", "animesh"]
    dict2 = {"data": nam}
    return render(request, "index2.html", dict2)

#def page1(request):
    #d1= render_to_string("P1.html")
    #return hr(d1)
    #return render(request, "p1.html")

def page1(request):

    return render(request, "P1.html")

def page2(request):
    d1= render_to_string("p2.html")
    return hr(d1)

def page3(request):
    d1= render_to_string("p3.html")
    return hr(d1)

def page4(request):
    d2= render_to_string("p4.html")
    return hr(d2)

def songnumber(request, snum):
    return hr("Searching for song no {}" .format(snum))

def studentdetails(request, name):
    return hr("yu want details about: {}".format(name))
#from .models import Albums as al


from .models import Album as al


def Album(request):
    data = al.objects.all()
    Dict={
        "albums":data
    }
    return render(request, "music/album2.html", Dict)


#from .models import *


#def myAlbum(request):
 #   data = Album.objects.all()
  #  Dict={
   #     "albums":data
    #}
    #return render(request, "music/album.html", Dict)

def AlbumDetails(requests, a_id):

    data = al.objects.get(id= a_id)
    songs = Songs.objects.filter(album_id=data)
    Dict = {
        "album":data, "Album_songs":songs
    }
    return render(requests, "music/albumdetails.html", Dict)


from .models import Songs as Songs
def SongList(request):
    all_songs = Songs.objects.all()
    Dict = {
        "songs":all_songs
    }
    return render(request, "music/SongsList.html", Dict)

from .models import College as Clg
def Coll(request):
    all_colleges = Clg.objects.all()
    Dict = {
        "college": all_colleges
    }
    return render(request, "music/CollegeList.html", Dict)

def Add_Album_old(request):
    if not request.user.is_authenticated:
        return redirect("login", 'addAlbum')
    else:
        if request.method == "POST":
            Dict = request.POST
            name = Dict["album_name"]
            artist = Dict["artist_name"]
            banner = request.FILES["album_banner"]
            Obj = al()
            Obj.name = name
            Obj.artist = artist
            Obj.image = banner
            Obj.save()
            return redirect("album")
    return render(request, "music/Add_Album.html")






def Add_Album(request):
    if not request.user.is_authenticated:
        return redirect("login", 'album')


    form = Add_Album_Form()
    if request.method == "POST":
        form = Add_Album_Form(request.POST)
        if form.is_valid():
            data = form.save(commit = False)
            data.artist = "Mr "+ data.artist
            data.save()
            return redirect('album')

    Dict = {"form":form}

    return render(request, "music/Add_Album.html", Dict)

def Delete_Album(request, a_id):
    if not request.user.is_authenticated:
        return redirect('login', 'album')
    data = al.objects.get(id = a_id)
    data.delete()
    return redirect('album')


def Edit_Album(request, a_id):

    album = al.objects.get(id = a_id)
    form  = Add_Album_Form(request.POST or None, request.FILES or None ,instance=album)
    if form.is_valid():
        form.save()
        return redirect('album')
    Dict = {
        "form":form
    }
    return render(request, 'music/Add_Album.html', Dict)

import time
def SubscribeUs(request):
    time.sleep(5)
    #if request.method == "POST":







def Add_NewSong(request):
    if request.method == "POST":
        data = request.POST
        song_title = data["song_title_name"]
        album_id  = data["album"]
        song_file = request.FILES["song_file"]
        album = al.objects.get(id = album_id)

        Songs.objects.create(title = song_title, album_id = album, file = song_file)

        #new_SONG = Songs()
        #new_SONG.title = song_title
        #new_SONG.album_id = album
        #new_SONG.file = song_file
        #new_SONG.save()
        return redirect("album")


    all_albums = al.objects.all().order_by("name")
    Dict = {
        "albums" : all_albums
    }
    return render(request, "music/Add_Song.html", Dict)


def Login(request, location):
    error = False
    last_un = ""
    if request.method == "POST":
        data = request.POST
        un = data['un']
        ps = data["ps"]
        last_un = un
        usr = authenticate(username = un, password = ps)
        if usr != None:
            login(request, usr)
            return redirect(location)
        error = True
    Dict = {
        "error":error, "last_un" : last_un
    }

    return render(request, "music/login.html", Dict)

def Logout(request):
    logout(request)
    return redirect('album')

def Register(request):
    if request.method == "POST":
        data = request.POST
        un = data['un']
        ps = data['ps']
        name = data['name']
        email = data['email']
        usr = User.objects.create_user(un, email, ps)
        usr.first_name = name
        usr.save()
        return redirect('login')

    return render(request, "music/register.html")

def Error_404(request, exception = True):
    return hr("My Error 404 Page")