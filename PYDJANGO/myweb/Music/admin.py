from django.contrib import admin

# Register your models here.
#from Music.models import Album
#from Music import *
#from Music.models import *
#from .models import Album

from .models import *

admin.site.register(Album)
admin.site.register(Songs)
admin.site.register(College)
admin.site.register(Students)