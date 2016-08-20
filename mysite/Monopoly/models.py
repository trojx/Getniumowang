from django.db import models

# Create your models here.

class chatcontent(models.Model):
    sharesname = models.CharField(max_length=16,null=True)
    time = models.DateTimeField(null=True)
    id = models.AutoField(models.IntegerField,primary_key=True)
    datapid = models.IntegerField(null=True)
    chattxt = models.TextField()