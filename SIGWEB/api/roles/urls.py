from django.urls import path
from api.roles import views


urlpatterns =[
    path('role/roleinfo/<int:pk>', views.role_detail),
    path('role/roleinfo/', views.role_list),
    path('role/rolecreate/', views.create)
]