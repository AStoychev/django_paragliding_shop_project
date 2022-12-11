from django.db import models

from enum import Enum

from django.contrib.auth import models as auth_models

from django.core import validators

from paragliding_shop.accounts.validators import MaxFileSizeInMbValidator, validate_only_alphanumeric
from django_countries.fields import CountryField


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    Female = "Female"
    Male = "Male"
    Neuter = "Neuter"


class AppUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LEN = 3
    FIRST_NAME_MAX_LEN = 15

    LAST_NAME_MIN_LEN = 3
    LAST_NAME_MAX_LEN = 15

    IMAGE_MAX_SIZE_IN_MB = 1.5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    MIN_LEN_GENDER = 2
    MAX_LEN_GENDER = 21

    MIN_VALUE_PRICE = 0.0

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_alphanumeric,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_alphanumeric,
        ),
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
    )
    # You have to install first CountryField (pip install django-countries)
    country = CountryField(
        null=False,
        blank=False,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    order = models.DecimalField(
        null=True,
        blank=True,
        max_digits=7,
        decimal_places=2,
        default=0,
        validators=(
            validators.MinValueValidator(MIN_VALUE_PRICE),
        ),
    )



    # Users log in with 'email'
    # USERNAME_FIELD = 'email'
