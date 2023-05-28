from django.db import models

# Create your models here.
class Plant(models.Model):
  name = models.CharField(max_length=200)
  type = models.CharField(max_length=100)
  water_needs = models.CharField(max_length=100)
  sun_needs = models.CharField(max_length=100)
  alive = models.BooleanField(default=True)

  def __str__(self):
    return self.name