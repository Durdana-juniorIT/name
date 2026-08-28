from django.db import models

class Blog(models.Model):
     first_name = models.CharField(max_length=255, verbose_name="Birinchi Nomi")
     about = models.TextField()

    #  age = models.IntegerField()
     age = models.PositiveBigIntegerField(default=12)
     total = models.BigIntegerField()

     height = models.FloatField(null=True, blank=True)

     married = models.BooleanField(default=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.first_name    