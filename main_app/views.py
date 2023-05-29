from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant

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
  return render(request, 'plants/detail.html', {'plant': plant})

class PlantCreate(CreateView):
  model = Plant
  fields = '__all__'
  success_url = '/plants/'

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['type', 'water_needs', 'sun_needs', 'alive']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'