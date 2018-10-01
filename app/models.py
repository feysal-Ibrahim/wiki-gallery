from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    objects=None
    name = models.CharField(max_length=60)

    def save_locations(self):
        self.save()

    def delete_locations(self):
        self.delete()

    def update_locations(self):
        self.update( )

    def __str__(self):
        return self.name

class Category(models.Model):
    objects=None
    name = models.CharField(max_length=60)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


    def update_category(self):
        self.update()


    def __str__(self):
        return self.name

class Image(models.Model):
    objects=None
    image = models.ImageField(upload_to = 'gallery/')
    image_name = models.CharField(max_length=30)
    image_url = models.TextField()
    description = models.TextField(blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    posted_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_name


    class Meta:
        ordering = ['posted_time']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update( )

    @classmethod
    def get_all(cls):
        images = cls.objects.order_by('posted_time')
        return images

    @classmethod
    def search_by_location(cls , search_term):
        image=cls.objects.filter( location__name__icontains=search_term )
        return image

    @classmethod
    def search_by_category(cls , search_term):
        image=cls.objects.filter( category__name__icontains=search_term )
        return image

    @classmethod
    def search_by_city(cls , search_term):
        image=cls.objects.filter( city__city__icontains=search_term )
        return image

    @classmethod
    def get_image_by_id(cls):
        Image.cls.objects.filter( id )
        return Image

    @classmethod
    def filter_by_location(cls , location):
        locations=cls.objects.filter( location=location )
        return locations

    @classmethod
    def filter_by_category(cls , category):
        categories=cls.objects.filter( categories=category )
        return categories