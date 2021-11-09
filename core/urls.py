from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register("currencies", views.CurrencyViewSet, basename="currency")


urlpatterns = [
    # path("", include(router.urls)),
    path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
    path(
        "currencies/<int:pk>/",
        views.CurrencyPKDetailAPIView.as_view(),
        name="currency-detail-pk",
    ),
    path(
        "currencies/<slug:slug>/",
        views.CurrencyDetailAllAPIView.as_view(),
        name="currency-detail-all",
    ),
    path(
        "currencies/<slug:slug>/latest/",
        views.CurrencyDetailLastAPIView.as_view(),
        name="currency-detail-latest",
    ),
    path(
        "currencies/<slug:slug>/<from_date>/<to_date>/",
        views.CurrencyDetailByDateAPIView.as_view(),
        name="currency-detail-by-date",
    ),
    path(
        "api_call_detail/<currency_code>/latest/",
        views.api_call_detail_latest,
        name="api-call-detail-latest",
    ),
    path(
        "api_call_detail/<currency_code>/<from_date>/<to_date>/",
        views.api_call_detail_by_date,
        name="api-call-detail-by-date",
    ),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
