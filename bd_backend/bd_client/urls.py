from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('persons', views.PersonsView, basename='persons')
router.register('firstname', views.FirstnameView, basename='firstname')
router.register('lastname', views.LastnameView, basename='lastname')
router.register('surname', views.SurnameView, basename='surname')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    #path('api/<action>/', views.personsApi)
]
