from django.contrib import admin
from core.models import Currency, APICall


class CurrencyAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "title",
        "price",
        "get_date",
    )
    list_display = ("id", "title", "price", "get_date")
    readonly_fields = ("id", "get_date", "title", "price")
    list_filter = ("title", "get_date")


class APICallAdmin(admin.ModelAdmin):
    fields = ("id", "user", "currency", "call_date")
    list_display = ("id", "user_id", "user", "currency_id", "currency", "call_date")
    readonly_fields = ("id", "user", "currency", "call_date")

    list_filter = ("currency__title", "call_date", "user")


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(APICall, APICallAdmin)
