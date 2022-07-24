from django.urls import path, include
from rest_framework import routers
from .views import ProjectsViewset

router = routers.DefaultRouter()
router.register('projects', ProjectsViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]