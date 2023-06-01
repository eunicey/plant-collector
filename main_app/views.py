from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Plant, Soil
from .forms import WateringForm

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def plant_index(request):
  plants = Plant.objects.filter(user=request.user)
  return render(request, 'plants/index.html', {'plants': plants})

@login_required
def plant_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  soils_plant_doesnt_have = Soil.objects.exclude(id__in = plant.soils.all().values_list('id'))

  watering_form= WateringForm()
  return render(request, 'plants/detail.html', {
    'plant': plant,
    'watering_form': watering_form,
    'soils': soils_plant_doesnt_have
  })

@login_required
def add_watering(request, plant_id):
  form = WateringForm(request.POST)
  if form.is_valid():
      new_watering = form.save(commit=False)
      new_watering.plant_id = plant_id
      new_watering.save()
  return redirect('plant-detail', plant_id=plant_id)

@login_required
def assoc_soil(request, plant_id, soil_id):
  Plant.objects.get(id=plant_id).soils.add(soil_id)
  return redirect('plant-detail', plant_id=plant_id)

class PlantCreate(LoginRequiredMixin, CreateView):
  model = Plant
  fields = ['name', 'size', 'water_needs', 'sun_needs', 'alive']

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
  model = Plant
  fields = ['size', 'water_needs', 'sun_needs', 'alive']

class PlantDelete(LoginRequiredMixin, DeleteView):
  model = Plant
  success_url = '/plants/'

class SoilCreate(LoginRequiredMixin, CreateView):
  model = Soil
  fields = '__all__'

class SoilList(LoginRequiredMixin, ListView):
  model = Soil

class SoilDetail(LoginRequiredMixin, DetailView):
  model = Soil

class SoilUpdate(LoginRequiredMixin, UpdateView):
  model = Soil
  fields = ['type', 'mixture']

class SoilDelete(LoginRequiredMixin, DeleteView):
  model = Soil
  success_url = '/soils/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('plant-index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)