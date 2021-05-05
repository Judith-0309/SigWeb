from django.urls import path
from api.point import views


urlpatterns =[
    path('point/pointinfo/<int:pk>', views.point_detail),
    path('point/pointinfo/', views.point_list),
    path('point/pointcreate/', views.create)

]