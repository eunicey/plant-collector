from django.db import models
from django.urls import reverse
from datetime import date, timedelta

SUNLIGHT = (
  ('L', 'Low'),
  ('M', 'Moderate'),
  ('B', 'Bright'),
)

WATER = (
  ('L', 'Low (every 2 weeks)'),
  ('M', 'Moderate (every week)'),
  ('H', 'High (2 times a week)'),
)

EXTRA_CARE = (
  ('R', 'Repot'),
  ('F', 'Fertilize'),
  ('P', 'Remove Pests'),
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
  
  def watered_today(self):
    return self.watering_set.filter(date=date.today()).count() >= 1

class Watering(models.Model):
  date = models.DateField('Watering date')
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
    # return f"{self.plant} - {self.date}"
    return self.date
  
  # change the default sort
  class Meta:
    ordering = ['-date']

class ExtraCare(models.Model):
  action = models.CharField(
    max_length=1,
    choices=EXTRA_CARE,
    default=EXTRA_CARE[1][0],
  )

  def __str__(self):
    return self.action
  
  def get_absolute_url(self):
    return reverse('extra_detail', kwargs={"pk": self.id})
