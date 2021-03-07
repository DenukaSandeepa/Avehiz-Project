from django.db import models
from django.contrib.auth.models import User


class publishing(models.Model):
      title = models.TextField(blank=True)
      pub_date = models.DateTimeField()
      type = models.TextField(blank=True)
      brand = models.TextField(blank=True)
      model = models.TextField(blank=True)
      year = models.IntegerField(default=0)
      fuel = models.TextField(blank=True)
      transmission = models.TextField(blank=True)
      milage = models.IntegerField(default=0)
      engine = models.TextField(blank=True)
      image = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/', blank=True)
      icon = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/', blank=True)
      description = models.CharField(max_length=250)
      condition = models.TextField(blank=True)
      price = models.IntegerField(default=0)
      tel = models.TextField(blank=True)
      city = models.TextField(blank=True)
      address = models.TextField(blank=True)
      vote_total = models.IntegerField(default=1)
      owner = models.ForeignKey(User,on_delete=models.CASCADE)

      def __str__(self):
          return self.title

      def summary(self):
          return self.body[:100]

      def pub_date_pretty(self):
          return pub_date.strftime('%b %e %y')
models.CharField(max_length=255)
