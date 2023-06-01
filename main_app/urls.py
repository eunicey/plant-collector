from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('plants/', views.plant_index, name='plant-index'),

  path('plants/<int:plant_id>/', views.plant_detail, name='plant-detail'),
  path('plants/<int:plant_id>/add-watering/', views.add_watering, name='add-watering'),
  path('plants/<int:plant_id>/assoc-soil/<int:soil_id>/', views.assoc_soil, name='assoc-soil'),

  path('accounts/signup/', views.signup, name='signup'),

  path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),
  path('plants/<int:pk>/update', views.PlantUpdate.as_view(), name='plant-update'),
  path('plants/<int:pk>/delete', views.PlantDelete.as_view(), name='plant-delete'),

  path('soils/create/', views.SoilCreate.as_view(), name='soil-create'),
  path('soils/<int:pk>/', views.SoilDetail.as_view(), name='soil-detail'),
  path('soils/', views.SoilList.as_view(), name='soil-index'),
  path('soils/<int:pk>/update/', views.SoilUpdate.as_view(), name='soil-update'),
  path('soils/<int:pk>/delete/', views.SoilDelete.as_view(), name='soil-delete'),
]
