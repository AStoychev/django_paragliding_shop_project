from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

from paragliding_shop.accounts.models import AppUser

UserModel = get_user_model()


class Product(models.Model):
    MAX_LEN_NAME = 200

    DECIMAL_PRICE_PLACE = 2

    MAX_PRICE_DIGITS = 8

    MIN_VALUE_PRICE = 0

    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )

    price = models.DecimalField(
        decimal_places=DECIMAL_PRICE_PLACE,
        max_digits=MAX_PRICE_DIGITS,
        validators=[MinValueValidator(MIN_VALUE_PRICE)]
    )

    def __str__(self):
        return self.name


class UserItem(models.Model):
    QUANTITY_DEFAULT = 1

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=QUANTITY_DEFAULT
    )

    added = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name
