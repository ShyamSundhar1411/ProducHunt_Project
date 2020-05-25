from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title=models.CharField(max_length=100)
    url=models.TextField(max_length=200,)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    body=models.TextField(max_length=1000)
    vote=models.IntegerField(default=1)
    hunter=models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:50]
    def pub_date_new(self):
        return self.pub_date.strftime('%b %e %Y')
