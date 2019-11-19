from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'scores', views.ScoreViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'professors', views.ProfessorViewSet)


urlpatterns = [
    path('', include(router.urls))
]
