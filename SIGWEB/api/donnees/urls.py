from django.urls import path
from api.donnees import views


urlpatterns =[
    path('donnees/donneesInfo/<int:pk>', views.donnees_detail),
    path('donnees/donneesInfo/', views.donnees_list),
    path('donnees/donneesrCreate/', views.donnees_create)
]