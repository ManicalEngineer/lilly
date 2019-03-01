from django.db import models

# Create your models here.
class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    album_name = models.ForeignKey('Album', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/', max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Cover(models.Model):
    album_name = models.OneToOneField(Album, on_delete=models.CASCADE, primary_key=True)
    image_id = models.ForeignKey('Image', on_delete=models.CASCADE)

    def __str__(self):
        return self.image_id
