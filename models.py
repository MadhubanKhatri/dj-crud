from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_married = models.CharField(max_length=30)

    def _str_(self):
        return self.first_name
