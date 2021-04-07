from django.urls import path
from api.compte import views


urlpatterns =[
    path('compteinfo/<int:pk>', views.compte_detail),
    path('compteinfo/', views.compte_list),

]