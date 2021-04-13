from django.urls import path
from api.polygone import views


urlpatterns =[
    path('polygone/polygoneinfo/<int:pk>', views.polygone_detail),
    path('polygone/polygoneinfo/', views.polygone_list),
    path('polygone/polygonecreate/', views.create)

]