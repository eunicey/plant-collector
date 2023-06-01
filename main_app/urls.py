from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('plants/', views.plant_index, name='plant-index'),
  path('plants/<int:plant_id>/', views.plant_detail, name='plant-detail'),
  path('plants/<int:plant_id>/add-watering/', views.add_watering, name='add-watering'),
  path('plants/<int:plant_id>/assoc-pot/<int:pot_id>/', views.assoc_pot, name='assoc-pot'),
  path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),
  path('plants/<int:pk>/update', views.PlantUpdate.as_view(), name='plant-update'),
  path('plants/<int:pk>/delete', views.PlantDelete.as_view(), name='plant-delete'),
  path('pots/create/', views.PotCreate.as_view(), name='pot-create'),
  path('pots/<int:pk>/', views.PotDetail.as_view(), name='pot-detail'),
  path('pots/', views.PotList.as_view(), name='pot-index'),
  path('pots/<int:pk>/update/', views.PotUpdate.as_view(), name='pot-update'),
  path('pots/<int:pk>/delete/', views.PotDelete.as_view(), name='pot-delete'),
]
