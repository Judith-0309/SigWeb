from django.urls import path
from api.user import views


urlpatterns =[
    path('user/userinfo/<int:pk>', views.user_detail),
    path('user/userinfo/', views.user_list),
    path('user/usercreate/', views.create)
]