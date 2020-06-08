from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50, blank=True)
    artist = models.CharField(max_length=50, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Songs(models.Model):
    title = models.CharField(max_length=50)
    #album_id = models.IntegerField(null=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    file = models.FileField(null=True)

    def __str__(self):
        return self.title

class College(models.Model):
    name = models.CharField(max_length = 40)
    add = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Students(models.Model):
    song = models.ForeignKey(Songs,on_delete=models.SET_NULL, null = True, blank=True)
    college = models.ForeignKey(College, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 40)
    branch = models.CharField(max_length= 30)

    def __str__(self):
        return self.name