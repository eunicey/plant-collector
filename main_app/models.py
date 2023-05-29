from django.db import models
from django.urls import reverse

SUNLIGHT = (
  ('L', 'Low'),
  ('M', 'Moderate'),
  ('B', 'Bright'),
)

WATER = (
  ('L', 'Low (drought tolerant)'),
  ('M', 'Moderate (every 1-2 weeks)'),
  ('H', 'High (2-3 times a week)'),
)

# Create your models here.
class Plant(models.Model):
  name = models.CharField(max_length=200)
  type = models.CharField(max_length=100)
  water_needs = models.CharField(
    max_length=1,
    choices=WATER,
    default=WATER[1][0],
  )
  sun_needs = models.CharField(
    max_length=1,
    choices=SUNLIGHT,
    default=SUNLIGHT[1][0],
  )
  alive = models.BooleanField(default=True)

  def __str__(self):
    return f"{self.name} - {self.type}"
  
  def get_absolute_url(self):
      return reverse("plant-detail", kwargs={"plant_id": self.id})
  
class Watering(models.Model):
  date = models.DateField('Watering date')
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.plant} - {self.date}"