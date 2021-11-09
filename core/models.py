from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework.reverse import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Currency(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=15, decimal_places=3)
    slug = models.SlugField()
    get_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Currency, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("currency-detail", args=(self.pk,))

    class Meta:
        verbose_name_plural = "currencies"
        ordering = ["-get_date"]


class APICall(models.Model):
    user = models.ForeignKey(
        User, related_name="user_api_calls", on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        Currency, related_name="currency_api_calls", on_delete=models.CASCADE
    )
    call_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -- {self.currency}"


# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
