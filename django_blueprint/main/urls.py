from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", views.UserAPIViewSet)
router.register(r"tasks", views.TaskAPIViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
