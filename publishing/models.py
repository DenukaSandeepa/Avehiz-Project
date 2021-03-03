from django.db import models
from django.contrib.auth.models import User

class Product(Models.model)
      title = models.CharField(max_length=255)
      pub_date = models.DateTimeField()
      boday = models.TextFeild()
      url = models.TextField()
      image = models.ImageField(upload_to='images/')
      icon = models.ImageField(upload_to='images/')
      vote_total = models.IntegerField(default=1)
      owner = models.ForeignKey(User,on_delete=models.CASCADE)

      def __str__(self):
          return self.title

      def summary(self):
          return self.body[:100]

      def pub_date_pretty(self):
          return pub_date.strftime('%b %e %y')
