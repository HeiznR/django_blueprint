from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"users", views.UserAPIViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
