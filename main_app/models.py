from django.db import models
from django.urls import reverse
from datetime import date

SUNLIGHT = (
  ('L', 'low'),
  ('M', 'moderate'),
  ('B', 'bright'),
)

WATER = (
  ('I', 'infrequent'),
  ('R', 'regular'),
  ('F', 'frequent'),
)

SOIL_TYPE = (
  ('I', 'Indoor'),
  ('O', 'Outdoor/Garden')
)


class Soil(models.Model):
  type = models.CharField(
    'Soil Mixture Type',
    max_length=1,
    choices=SOIL_TYPE,
    default=SOIL_TYPE[0][0]
  )
  mixture = models.CharField('Soil Composition and Additives', max_length=100)
  
  def __str__(self):
    return f"{self.type} - {self.mixture}"
  
  def get_absolute_url(self):
    return reverse('soil-detail', kwargs={"pk": self.id})


class Plant(models.Model):
  name = models.CharField(max_length=200)
  type = models.CharField(max_length=100)
  water_needs = models.CharField(
    'Watering Needs',
    max_length=1,
    choices=WATER,
    default=WATER[1][0],
  )
  sun_needs = models.CharField(
    max_length=1,
    choices=SUNLIGHT,
    default=SUNLIGHT[1][0],
  )
  alive = models.BooleanField('Still Alive?', default=True)
  soils = models.ManyToManyField(Soil)

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
    return f"{self.plant} - {self.date}"
  
  class Meta:
    ordering = ['-date']
