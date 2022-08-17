from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'

