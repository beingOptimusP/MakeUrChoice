from django.db import models

# Create your models here.
class CreatPoll(models.Model):
    Title = models.TextField()
    o1 = models.TextField()
    o2 = models.TextField()
    o3 = models.TextField()
    o4 = models.TextField()
    on1= models.IntegerField(default=0)
    on2= models.IntegerField(default=0)
    on3= models.IntegerField(default=0)
    on4= models.IntegerField(default=0)
    one_1=models.IntegerField(default=0)
    two_1=models.IntegerField(default=0)
    three_1=models.IntegerField(default=0)
    four_1=models.IntegerField(default=0)
    votes=models.IntegerField(default=0)
    


class OpenPoll(models.Model):
    title = models.TextField()
    o1 = models.TextField()
    o2 = models.TextField()
    o3 = models.TextField()
    o4 = models.TextField()
    on1= models.IntegerField(default=0)
    on2= models.IntegerField(default=0)
    on3= models.IntegerField(default=0)
    on4= models.IntegerField(default=0)
    votes=models.IntegerField(default=0)

