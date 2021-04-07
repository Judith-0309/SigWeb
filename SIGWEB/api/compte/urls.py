from django.urls import path
from api.compte import views


urlpatterns =[
    path('compte/compteinfo/<int:pk>', views.compte_detail),
    path('compte/compteinfo/', views.compte_list),
    path('compte/comptecreate/', views.create)

]