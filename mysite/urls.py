from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView().as_view(), name="token_refresh"),
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
