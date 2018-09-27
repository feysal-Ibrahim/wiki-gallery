from django.db import models
import datetime as dt

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    image_name = models.CharField(max_length=30)
    image_url = models.TextField()
    description = models.TextField(blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    posted_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['posted_time']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, target, update):
        updated = cls.objects.filter(id=id).update(target=update)
        return updated

    @classmethod
    def get_all(cls):
        images = cls.objects.order_by('posted_time')
        return images

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search(cls, query):
        result = cls.objects.filter(description__icontains=query).order_by('image_name')
        return result

    @classmethod
    def search_by_category(cls, search_term):
        display = cls.objects.filter(category__name__icontains=search_term)
        return display

    @classmethod
    def filter_by_location(cls, search_term):
        display = cls.objects.filter(location__name__icontains=search_term)
        return display

class Location(models.Model):
    name = models.CharField(max_length=60)

    def save_locations(self):
        self.save()

    def delete_locations(self):
        self.delete()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=60)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

