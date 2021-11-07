from django.db import models


# class Category(models.Model):
#     pass


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile/images')

    def __str__(self):
        return self.first_name


class Movie(models.Model):  # My table in the database

    # slug = models.SlugField()
    active = models.BooleanField(default=True)

    name = models.CharField("Movie Name", max_length=255, unique=True)  # my first column in the table

    description = models.TextField(verbose_name="Movie Description")

    likes = models.IntegerField(default=0, null=True)

    watch_count = models.IntegerField(default=0, null=True)

    rate = models.PositiveIntegerField(default=0, null=True)

    production_date = models.DateField(null=True, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    modification_date = models.DateTimeField(auto_now=True)

    poster = models.ImageField(upload_to='movie/images')

    video = models.FileField(upload_to='movie/videos')

    def __str__(self):
        return self.name
