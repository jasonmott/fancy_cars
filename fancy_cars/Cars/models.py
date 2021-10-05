from django.db import models
from django.urls import reverse

# Create your models here.

class Cars(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(max_length=4,blank=True)
    price = models.FloatField(blank=True)
    origin = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    horsepower = models.IntegerField(max_length=4,blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)   
    active = models.BooleanField(default=True)

    def __str__(self):
        # need self - difference between function and a method -- method uses s$
        #return str(self.title) - If you just want to use title
        # This changes to POST Title from the site  -- Adds the two fields
        return "{} {} - {}".format(self.make, self.model, self.year)

    def get_absolute_url(self):
        # calling PostDetail pattern from the urls.py file. kwars is key word search
        return reverse("CarDetailView", kwargs={"pk": self.pk})