from django.urls import path
from api.user import views


urlpatterns =[
    path('userinfo/<int:pk>', views.user_detail),
    path('userinfo/', views.user_list),
    path('usercreate/', views.user_create)
]