from rest_framework import serializers

from .models import Currency, APICall


class CurrencyListSerializer(serializers.HyperlinkedModelSerializer):
    # detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        fields = (
            "id",
            "title",
            "slug",
            "url",
            "price",
            "get_date",
        )
        extra_kwargs = {
            "url": {"view_name": "currency-detail-pk", "lookup_field": "pk"},
        }

    # def get_detail_url(self, obj):
    #     return obj.get_absolute_url()


class CurrencyDetailSerializer(serializers.ModelSerializer):
    # detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        lookup_field = "slug"
        fields = (
            "id",
            "title",
            "slug",
            "price",
            "get_date",
        )
        extra_kwargs = {
            "url": {"lookup_field": "pk"},
        }

    # def get_detail_url(self, obj):
    #     return obj.get_absolute_url()
