from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^', include('api.user.urls')),
    url(r'^', include('api.compte.urls')),
    url(r'^', include('api.roles.urls')),
    url(r'^', include('api.donnees.urls')),
    url(r'^', include('api.points.urls')),
    url(r'^', include('api.ligne.urls')),
    url(r'^', include('api.polygone.urls')),
    url(r'^', include('api.donnees_raster.urls')),

]
