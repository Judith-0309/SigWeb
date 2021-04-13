from django.urls import path
from api.ligne import views


urlpatterns =[
    path('ligne/ligneinfo/<int:pk>', views.ligne_detail),
    path('ligne/ligneinfo/', views.ligne_list),
    path('ligne/lignecreate/', views.create)

]