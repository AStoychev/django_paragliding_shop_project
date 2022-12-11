from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from paragliding_shop.accounts.models import AppUser


class ProfileModelTests(TestCase):

    def test_profile_save_when_first_name_is_valid(self):
        profile = AppUser(
            username='Peshov',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            image='profiles/Profilna_15rwfTg.jpg',
            age=18,
            country='BG',
            gender='Male',
        )

        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile.pk)

    def test_profile_save_when_first_name_is_not_valid_expect_to_fail(self):
        profile = AppUser(
            username='Peshov',
            password='asdfasdf',
            first_name='Pesho123_3123',
            last_name='Peshov',
            email='pesho@abv.bg',
            age=18,
            country='BG',
            gender='Male',
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save_when_last_name_is_not_valid_expect_to_fail(self):
        profile = AppUser(
            username='Peshov',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov231_1231e',
            email='pesho@abv.bg',
            age=18,
            country='BG',
            gender='Male',
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save_when_username_is_unique_expect_to_valid(self):
        profile = AppUser(
            username='Pesho',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            age=18,
            country='BG',
            gender='Male',
        )

        profile.full_clean()
        profile.save()

    def test_profile_save_when_username_is_valid(self):
        first_profile = AppUser(
            username='Pesho',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            age=18,
            country='BG',
            gender='Male',
        )

        second_profile = AppUser(
            username='Gosho',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='gosho@abv.bg',
            age=18,
            country='BG',
            gender='Male',
        )

        first_profile.full_clean()
        second_profile.full_clean()
        first_profile.save()
        second_profile.save()

    def test_profile_save_when_username_is_not_unique_expect_to_fail(self):
        first_profile = AppUser(
            username='Pesho',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            age=18,
            country='BG',
            gender='Male',
        )

        second_profile = AppUser(
            username='Pesho',
            password='asdfasdf',
            first_name='Gosho',
            last_name='Goshov',
            email='gosho@abv.bg',
            age=18,
            country='BG',
            gender='Male',
        )

        with self.assertRaises(IntegrityError) as context:
            first_profile.full_clean()
            second_profile.full_clean()
            first_profile.save()
            second_profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save_when_image_is_above_permitted_size_valid(self):
        profile = AppUser(
            username='Peshov',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            image='profiles/msg-1-fc-40.jpg',
            age=18,
            country='BG',
            gender='Male',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save_when_email_is_not_unique_expect_to_fail(self):
        first_profile = AppUser(
            username='Peshov',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            age=18,
            country='BG',
            gender='Male',
        )

        second_profile = AppUser(
            username='Gocho',
            password='asdfasdf',
            first_name='Gosho',
            last_name='Goshov',
            email='pesho@abv.bg',
            age=18,
            country='BG',
            gender='Male',
        )

        with self.assertRaises(IntegrityError) as context:
            first_profile.full_clean()
            second_profile.full_clean()
            first_profile.save()
            second_profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save_when_age_is_zero_number_expect_to_valid(self):
        profile = AppUser(
            username='Peshov',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            age=0,
            country='BG',
            gender='Male',
        )

        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile.pk)

    def test_profile_save_when_age_is_negative_number_expect_to_fail(self):
        profile = AppUser(
            username='Peshov',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            age=-18,
            country='BG',
            gender='Male',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save_when_country_is_written_in_bg_name_expect_to_fail(self):
        profile = AppUser(
            username='Peshov',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            age=18,
            country='България',
            gender='Male',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save_when_country_is_not_valid_name_expect_to_fail(self):
        profile = AppUser(
            username='Peshov',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            age=18,
            country='Bulggaria',
            gender='Male',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save_when_gender_is_not_valid_option_expect_to_fail(self):
        profile = AppUser(
            username='Peshov',
            password='asdfasdf',
            first_name='Pesho',
            last_name='Peshov',
            email='pesho@abv.bg',
            age=18,
            country='BG',
            gender='Man',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)