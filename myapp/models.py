from django.db import models


class shop1(models.Model):
    eid=models.CharField(max_length=10,auto_created=True)
    name=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    Email=models.EmailField()
    contact=models.CharField(max_length=12)


