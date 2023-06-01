from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant, Soil
from .forms import WateringForm

# class Plant:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, type, water_needs, sun_needs, alive):
#     self.name = name
#     self.type = type
#     self.water_needs = water_needs
#     self.sun_needs = sun_needs
#     self.alive = alive

# plants = [
#   Plant('Aloe', 'succulent', 'low', 'bright', True),
#   Plant('Birds Nest Fern', 'fern', 'moderate', 'moderate', False),
#   Plant('Bromeliad', 'monocot flowering', 'low', 'low', True),
#   Plant('Croton', 'shrub', 'moderate', 'bright', False)
# ]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def plant_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', {'plants': plants})

def plant_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  soils_plant_doesnt_have = Soil.objects.exclude(id__in = plant.soils.all().values_list('id'))

  watering_form= WateringForm()
  return render(request, 'plants/detail.html', {
    'plant': plant,
    'watering_form': watering_form,
    'soils': soils_plant_doesnt_have
  })

def add_watering(request, plant_id):
  form = WateringForm(request.POST)
  if form.is_valid():
      new_watering = form.save(commit=False)
      new_watering.plant_id = plant_id
      new_watering.save()
  return redirect('plant-detail', plant_id=plant_id)

class PlantCreate(CreateView):
  model = Plant
  fields = ['name', 'type', 'water_needs', 'sun_needs', 'alive']
  success_url = '/plants/'

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['type', 'water_needs', 'sun_needs', 'alive']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'

class SoilCreate(CreateView):
  model = Soil
  fields = '__all__'

class SoilList(ListView):
  model = Soil

class SoilDetail(DetailView):
  model = Soil

class SoilUpdate(UpdateView):
  model = Soil
  fields = ['type', 'mixture']

class SoilDelete(DeleteView):
  model = Soil
  success_url = '/soils/'

def assoc_soil(request, plant_id, soil_id):
  Plant.objects.get(id=plant_id).soils.add(soil_id)
  return redirect('plant-detail', plant_id=plant_id)