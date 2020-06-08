"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Music.views import Home
from Music.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500


#imports everything from views.py
#from Music.views import p2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myhome/', Home, name = "h"),
    path('mypage/', page1, name="pg1"),
    path('jetix/', page2, name="pg2"),
    path('hungama/', page3, name="pg3"),
    path('cn/', page4, name="pg4"),

    path('song/<int:snum>/', songnumber, name='Songs'),
    path('details/<str:name>/', studentdetails, name="students"),
    path('', Home2, name=""),
    #myalbum


    path('myalbum/', Album, name='album'),
    path('albumdetails/<int:a_id>/', AlbumDetails, name='details'),
    path('all_songs/', SongList, name = "Allsongs"),
    path('all_colleges/', Coll , name = "Allcolleges"),
    path('add_album/', Add_Album, name = "addAlbum"),
    path('delete_album/<int:a_id>', Delete_Album, name = "deleteAlbum"),
    path('edit_album/<int:a_id>', Edit_Album, name = "editAlbum"),
    path('add_song/', Add_NewSong, name = "addSong"),
    path('Login_Account/<str:location>/', Login, name = "login"),
    path('Logout_Account/', Logout, name = "logout"),
    path('Register_Account/', Register, name = "register"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = Error_404()

