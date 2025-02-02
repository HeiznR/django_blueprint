from django.urls import include, path
from . import views
from .views import SignupView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r"users", views.UserAPIViewSet)
router.register(r"tasks", views.TaskAPIViewSet)

urlpatterns = [
    path("api/v1/signup/", SignupView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/", include(router.urls)),
]
