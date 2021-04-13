from django.urls import path
from api.donnees_raster import views


urlpatterns = [
    path('donneesRaster/donneesRasterinfo/<int:pk>', views. donneesRaster_detail),
    path('donneesRaster/donneesRasterinfo/', views. donneesRaster_list),
    path('donneesRaster/donneesRastercreate/', views.create)

 ]