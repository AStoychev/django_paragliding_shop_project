from django.contrib.auth import get_user_model
from django.core import validators
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from paragliding_shop.equipment.model_choices import WingsCertificationChoices, ConditionChoices, WingTestChoices, \
    HarnessCategoryChoices, ReservesTypeChoices, InstrumentsChoices, HelmetVisorChoices


UserModel = get_user_model()


class Wings(models.Model):
    MAX_LEN_MANUFACTURER = 30
    MIN_LEN_MANUFACTURER = 2

    MAX_LEN_MODEL = 30
    MIN_LEN_MODEL = 1

    MAX_LEN_CONDITION = 10
    MIN_LEN_CONDITION = 2

    MAX_LEN_URL_FIELD = 1000

    MIN_VALUE_PRICE = 0.0

    MAX_VALUE_POROSITY = 1000
    MIN_VALUE_POROSITY = 10

    manufacturer = models.CharField(
        max_length=MAX_LEN_MANUFACTURER,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MANUFACTURER),
        ),
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MODEL),
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        max_length=MAX_LEN_URL_FIELD,
        null=False,
        blank=False,
        verbose_name="Image URL",
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_VALUE_PRICE),
        ),
    )

    en_certification = models.CharField(
        choices=WingsCertificationChoices.choices(),
        max_length=WingsCertificationChoices.max_len(),
        null=False,
        blank=False,
    )

    year = models.DateField(
        null=True,
        blank=True,
    )

    condition = models.CharField(
        choices=ConditionChoices.choices(),
        max_length=ConditionChoices.max_len(),
        null=False,
        blank=False,
    )

    test = models.CharField(
        choices=WingTestChoices.choices(),
        max_length=WingTestChoices.max_len(),
        null=False,
        blank=False,
    )

    porosity = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=(
            MaxValueValidator(MAX_VALUE_POROSITY),
            MinValueValidator(MIN_VALUE_POROSITY),
        )
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Harness(models.Model):
    MAX_LEN_MANUFACTURER = 30
    MIN_LEN_MANUFACTURER = 2

    MAX_LEN_MODEL = 30
    MIN_LEN_MODEL = 1

    MAX_LEN_URL_FIELD = 1000

    MIN_VALUE_PRICE = 0.0

    manufacturer = models.CharField(
        max_length=MAX_LEN_MANUFACTURER,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MANUFACTURER),
        ),
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MODEL),
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        max_length=MAX_LEN_URL_FIELD,
        null=False,
        blank=False,
        verbose_name="Image URL",
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_VALUE_PRICE),
        ),
    )

    category = models.CharField(
        choices=HarnessCategoryChoices.choices(),
        max_length=HarnessCategoryChoices.max_len(),
        null=False,
        blank=False,
    )

    condition = models.CharField(
        choices=ConditionChoices.choices(),
        max_length=ConditionChoices.max_len(),
        null=False,
        blank=False,
    )

    year = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Reserves(models.Model):
    MAX_LEN_MANUFACTURER = 30
    MIN_LEN_MANUFACTURER = 2

    MAX_LEN_MODEL = 30
    MIN_LEN_MODEL = 1

    MAX_LEN_URL_FIELD = 1000

    MIN_VALUE_PRICE = 0.0

    manufacturer = models.CharField(
        max_length=MAX_LEN_MANUFACTURER,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MANUFACTURER),
        ),
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MODEL),
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        max_length=MAX_LEN_URL_FIELD,
        null=False,
        blank=False,
        verbose_name="Image URL",
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_VALUE_PRICE),
        ),
    )

    type = models.CharField(
        choices=ReservesTypeChoices.choices(),
        max_length=ReservesTypeChoices.max_len(),
        null=False,
        blank=False,
    )

    year = models.DateField(
        null=True,
        blank=True,
    )

    condition = models.CharField(
        choices=ConditionChoices.choices(),
        max_length=ConditionChoices.max_len(),
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Instruments(models.Model):
    MAX_LEN_MANUFACTURER = 30
    MIN_LEN_MANUFACTURER = 2

    MAX_LEN_URL_FIELD = 1000

    MIN_VALUE_PRICE = 0.0

    manufacturer = models.CharField(
        max_length=MAX_LEN_MANUFACTURER,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MANUFACTURER),
        ),
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        max_length=MAX_LEN_URL_FIELD,
        null=False,
        blank=False,
        verbose_name="Image URL",
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_VALUE_PRICE),
        ),
    )

    type = models.CharField(
        choices=InstrumentsChoices.choices(),
        max_length=InstrumentsChoices.max_len(),
        null=False,
        blank=False,
    )
    condition = models.CharField(
        choices=ConditionChoices.choices(),
        max_length=ConditionChoices.max_len(),
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Helmets(models.Model):
    MAX_LEN_MANUFACTURER = 30
    MIN_LEN_MANUFACTURER = 2

    MAX_LEN_URL_FIELD = 1000

    MIN_VALUE_PRICE = 0.0

    MAX_LEN_TYPE = 30

    manufacturer = models.CharField(
        max_length=MAX_LEN_MANUFACTURER,
        validators=(
            validators.MinLengthValidator(MIN_LEN_MANUFACTURER),
        ),
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        max_length=MAX_LEN_URL_FIELD,
        null=False,
        blank=False,
        verbose_name="Image URL",
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_VALUE_PRICE),
        ),
    )

    visor = models.CharField(
        choices=HelmetVisorChoices.choices(),
        max_length=HelmetVisorChoices.max_len(),
        null=False,
        blank=False,
    )
    condition = models.CharField(
        choices=ConditionChoices.choices(),
        max_length=ConditionChoices.max_len(),
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )