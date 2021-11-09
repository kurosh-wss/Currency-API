import json
import datetime
from decimal import Decimal
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .serializers import CurrencyListSerializer, CurrencyDetailSerializer
from .models import Currency, APICall
from .scraper import get_currencies
from .permissions import IsCustomer


class CurrencyListAPIView(generics.ListAPIView):
    serializer_class = CurrencyListSerializer
    queryset = Currency.objects.all()
    permission_classes = [IsAdminUser]


class CurrencyDetailAllAPIView(generics.ListAPIView):
    serializer_class = CurrencyListSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        slug = self.kwargs["slug"]
        currency = Currency.objects.filter(slug=slug)
        return currency


class CurrencyDetailLastAPIView(generics.RetrieveAPIView):
    serializer_class = CurrencyDetailSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        slug = self.kwargs["slug"]
        cur = Currency.objects.filter(title=slug.upper())
        currency = (
            Currency.objects.filter(title=slug.upper()).order_by("-get_date").first()
        )
        qs = Currency.objects.filter(pk=currency.pk)
        return qs


class CurrencyPKDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CurrencyDetailSerializer
    queryset = Currency.objects.all()
    permission_classes = [IsAdminUser]


class CurrencyDetailByDateAPIView(generics.RetrieveAPIView):
    serializer_class = CurrencyDetailSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        slug, from_date, to_date = self.kwargs.values()
        if not from_date:
            from_date = datetime.date.min
        if not to_date:
            to_date = datetime.date.max
        cur = Currency.objects.filter(title=slug.upper())
        currency = (
            Currency.objects.filter(title=slug.upper())
            .filter(get_date__range=(from_date, to_date))
            .first()
        )
        qs = Currency.objects.filter(pk=currency.pk)
        return qs


@api_view(["GET"])
@permission_classes([IsCustomer])
def api_call_detail_latest(request, currency_code, format=None):
    if request.method == "GET":
        # Calling scraper function to update currency database
        currencies = get_currencies()
        if currencies:
            try:
                for code, price in currencies.items():
                    # Creating new currency objects
                    if code == currency_code:
                        currency = Currency.objects.create(
                            title=code.upper(),
                            price=price,
                        )
                    else:
                        Currency.objects.create(
                            title=code.upper(),
                            price=price,
                        )
                # Create APICall objects for requested currency
                APICall.objects.create(user=request.user, currency=currency)
                serializer = CurrencyDetailSerializer(currency)
                return Response(serializer.data)

            except KeyError:
                # Retreive data from database if there is a problem in dictionary
                currency = (
                    Currency.objects.filter(title=currency_code.upper())
                    .order_by("-get_date")
                    .first()
                )
                APICall.objects.create(user=request.user, currency=currency)
                serializer = CurrencyDetailSerializer(currency)
                return Response(serializer.data)

        else:
            # Retreive data from database if the scraper call failed
            currency = (
                Currency.objects.filter(title=currency_code.upper())
                .order_by("-get_date")
                .first()
            )
            APICall.objects.create(user=request.user, currency=currency)
            serializer = CurrencyDetailSerializer(currency)
            return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsCustomer])
def api_call_detail_by_date(request, currency_code, from_date, to_date, format=None):
    if request.method == "GET":
        # Retreive data from database
        if from_date is None:
            from_date = datetime.date.min
        if to_date is None:
            to_date = datetime.date.max

        currency = (
            Currency.objects.filter(slug=currency_code)
            .filter(get_date__range=(from_date, to_date))
            .first()
        )

        if currency is not None:
            serializer = CurrencyDetailSerializer(currency)
            APICall.objects.create(user=request.user, currency=currency)
            return Response(serializer.data)
        else:
            serializer = {
                "has_error": 1,
                "error_message": "Couldn't find currency in the specified date rage.",
            }
            return Response(serializer)
