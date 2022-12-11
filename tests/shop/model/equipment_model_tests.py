from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from paragliding_shop.accounts.models import AppUser
from paragliding_shop.equipment.models import Wings, Harness, Reserves, Instruments, Helmets


class ProfileModelTests(TestCase):
    user = AppUser(
        username="Pesho",
        email="pesho@abv.bg",
        age=30,
        country="BG",
    )

    def test_wing_save_when_data_is_valid(self):
        self.user.save()

        wing = Wings(
            manufacturer='Advance',
            model='Omega',
            price=3000,
            en_certification='EN_A',
            image_url='https://media.glamour.com/photos/62ac98eb9ca0311618a5bd8c/16:9/w_1280,c_limit/1153778013',
            year="2015-10-10",
            condition="New",
            test='Yes',
            porosity=300,
            user=self.user
        )

        wing.full_clean()
        wing.save()

        self.assertIsNotNone(wing.pk)

    def test_wing_save_when_data_is_not_valid(self):
        self.user.save()
        wing = Wings(
            manufacturer='',
            model='Omega',
            price=-3000,
            en_certification='EN_A',
            image_url='https://media.glamour.com/photos/62ac98eb9ca0311618a5bd8c/16:9/w_1280,c_limit/1153778013',
            year="2015-10-10",
            condition="New",
            test='Yes',
            porosity=300,
            user=self.user
        )

        with self.assertRaises(ValidationError) as context:
            wing.full_clean()
            wing.save()

        self.assertIsNotNone(context.exception)

    def test_wing_save_when_not_image(self):
        self.user.save()
        wing = Wings(
            manufacturer='Advance',
            model='Omega',
            price=3000,
            en_certification='EN_A',
            image_url='',
            year="2015-10-10",
            condition="New",
            test='Yes',
            porosity=300,
            user=self.user
        )

        with self.assertRaises(ValidationError) as context:
            wing.full_clean()
            wing.save()

        self.assertIsNotNone(context.exception)

    def test_harness_save_when_data_is_valid(self):
        self.user.save()
        harness = Harness(
            manufacturer='Advance',
            model='Omega',
            price=3000,
            image_url='https://media.glamour.com/photos/62ac98eb9ca0311618a5bd8c/16:9/w_1280,c_limit/1153778013',
            year="2015-10-10",
            category="Mountain",
            condition="New",
            user=self.user
        )

        harness.full_clean()
        harness.save()

        self.assertIsNotNone(harness.pk)

    def test_harness_save_when_data_is_not_valid(self):
        self.user.save()
        harness = Harness(
            manufacturer='',
            model='',
            price=-3000,
            image_url='https://media.glamour.com/photos/62ac98eb9ca0311618a5bd8c/16:9/w_1280,c_limit/1153778013',
            year="2015-10-10",
            category="Mountain",
            condition="New",
            user=self.user
        )

        with self.assertRaises(ValidationError) as context:
            harness.full_clean()
            harness.save()

        self.assertIsNotNone(context.exception)

    def test_harness_save_when_not_image(self):
        self.user.save()
        harness = Harness(
            manufacturer='Advance',
            model='Omega',
            price=3000,
            image_url='',
            year="2015-10-10",
            condition="New",
            user=self.user
        )

        with self.assertRaises(ValidationError) as context:
            harness.full_clean()
            harness.save()

        self.assertIsNotNone(context.exception)

    def test_reserves_save_when_data_is_valid(self):
        self.user.save()
        reserves = Reserves(
            manufacturer='Advance',
            model='Omega',
            price=3000,
            image_url='https://media.glamour.com/photos/62ac98eb9ca0311618a5bd8c/16:9/w_1280,c_limit/1153778013',
            type="Standard",
            year="2015-10-10",
            condition="New",
            user=self.user
        )

        reserves.full_clean()
        reserves.save()

        self.assertIsNotNone(reserves.pk)

    def test_reserves_save_when_data_is_not_valid(self):
        self.user.save()
        reserves = Reserves(
            manufacturer='',
            model='',
            price=-3000,
            image_url='https://media.glamour.com/photos/62ac98eb9ca0311618a5bd8c/16:9/w_1280,c_limit/1153778013',
            type="Standard",
            year="2015-10-10",
            condition="New",
            user=self.user
        )

        with self.assertRaises(ValidationError) as context:
            reserves.full_clean()
            reserves.save()

        self.assertIsNotNone(context.exception)

    def test_reserves_save_when_not_image(self):
        self.user.save()
        reserves = Reserves(
            manufacturer='Advance',
            model='Omega',
            price=3000,
            image_url='',
            type="Standard",
            year="2015-10-10",
            condition="New",
            user=self.user
        )

        with self.assertRaises(ValidationError) as context:
            reserves.full_clean()
            reserves.save()

        self.assertIsNotNone(context.exception)

    def test_instruments_save_when_data_is_valid(self):
        self.user.save()
        instruments = Instruments(
            manufacturer='Advance',
            price=3000,
            image_url='https://media.glamour.com/photos/62ac98eb9ca0311618a5bd8c/16:9/w_1280,c_limit/1153778013',
            type="AltiVariosGPS",
            condition="New",
            user=self.user
        )

        instruments.full_clean()
        instruments.save()

        self.assertIsNotNone(instruments.pk)

    def test_instruments_save_when_data_is_not_valid(self):
        self.user.save()
        instruments = Instruments(
            manufacturer='',
            price=-3000,
            image_url='https://media.glamour.com/photos/62ac98eb9ca0311618a5bd8c/16:9/w_1280,c_limit/1153778013',
            type="AltiVariosGPS",
            condition="New",
            user=self.user
        )

        with self.assertRaises(ValidationError) as context:
            instruments.full_clean()
            instruments.save()

        self.assertIsNotNone(context.exception)

    def test_instruments_save_when_not_image(self):
        self.user.save()
        instruments = Instruments(
            manufacturer='Advence',
            price=3000,
            image_url='',
            type="AltiVariosGPS",
            condition="New",
            user=self.user
        )

        with self.assertRaises(ValidationError) as context:
            instruments.full_clean()
            instruments.save()

        self.assertIsNotNone(context.exception)

    def test_helmet_save_when_data_is_valid(self):
        self.user.save()
        helmet = Helmets(
            manufacturer='Advance',
            price=3000,
            image_url='https://media.glamour.com/photos/62ac98eb9ca0311618a5bd8c/16:9/w_1280,c_limit/1153778013',
            visor="Yes",
            condition="New",
            user=self.user
        )

        helmet.full_clean()
        helmet.save()

        self.assertIsNotNone(helmet.pk)

    def test_helmet_save_when_data_is_not_valid(self):
        self.user.save()
        helmet = Helmets(
            manufacturer='',
            price=-3000,
            image_url='https://media.glamour.com/photos/62ac98eb9ca0311618a5bd8c/16:9/w_1280,c_limit/1153778013',
            visor="Yes",
            condition="New",
            user=self.user
        )

        with self.assertRaises(ValidationError) as context:
            helmet.full_clean()
            helmet.save()

        self.assertIsNotNone(context.exception)

    def test_helmet_save_when_not_image(self):
        self.user.save()
        helmet = Helmets(
            manufacturer='Advance',
            price=3000,
            image_url='',
            visor="Yes",
            condition="New",
            user=self.user
        )

        with self.assertRaises(ValidationError) as context:
            helmet.full_clean()
            helmet.save()

        self.assertIsNotNone(context.exception)