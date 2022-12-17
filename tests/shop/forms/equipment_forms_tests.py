from django.test import TestCase

from paragliding_shop.equipment.forms import CreateWingForm, EditWingForm, CreateHarnessesForm, EditHarnessesForm, \
    CreateReservesForm, EditReservesForm, CreateInstrumentsForm, EditInstrumentsForm, CreateHelmetsForm, EditHelmetsForm


class EquipmentCreateEditFormTests(TestCase):

    def test_create_form_successfully_wing(self):
        data = {
            'manufacturer': 'Advance',
            'model': 'Bi2',
            'image_url': 'https://ojovolador.com/wp-content/uploads/2019/07/ADVANCE_OMEGA_XALPS_HEAD.jpg',
            'price': 3000,
            'en_certification': 'EN_A',
            'year': '2015-10-10',
            "condition": "New",
            "test": 'Yes',
            "porosity": 300,
        }

        form = CreateWingForm(data)

        self.assertTrue(form.is_valid())

    def test_create_form_failed_wing_with_negative_price(self):
        data = {
            'manufacturer': 'Advance',
            'model': 'Bi2',
            'image_url': 'https://ojovolador.com/wp-content/uploads/2019/07/ADVANCE_OMEGA_XALPS_HEAD.jpg',
            'price': -3000,
            'en_certification': 'EN_A',
            'year': '2015-10-10',
            "condition": "New",
            "test": 'Yes',
            "porosity": 300,
        }

        form = CreateWingForm(data)

        self.assertFalse(form.is_valid())

    def test_create_form_failed_wing_without_manufacture(self):
        data = {
            'manufacturer': '',
            'model': 'Bi2',
            'image_url': 'https://ojovolador.com/wp-content/uploads/2019/07/ADVANCE_OMEGA_XALPS_HEAD.jpg',
            'price': -3000,
            'en_certification': 'EN_A',
            'year': '2015-10-10',
            "condition": "New",
            "test": 'Yes',
            "porosity": 300,
        }

        form = CreateWingForm(data)

        self.assertFalse(form.is_valid())

    def test_create_form_failed_wing_with_negative_porosity(self):
        data = {
            'manufacturer': 'Advance',
            'model': 'Bi2',
            'image_url': 'https://ojovolador.com/wp-content/uploads/2019/07/ADVANCE_OMEGA_XALPS_HEAD.jpg',
            'price': 3000,
            'en_certification': 'EN_A',
            'year': '2015-10-10',
            "condition": "New",
            "test": 'Yes',
            "porosity": -300,
        }

        form = CreateWingForm(data)

        self.assertFalse(form.is_valid())

    def test_create_form_failed_wing_with_wrong_placeholder_from_date(self):
        data = {
            'manufacturer': 'Advance',
            'model': 'Bi2',
            'image_url': 'https://ojovolador.com/wp-content/uploads/2019/07/ADVANCE_OMEGA_XALPS_HEAD.jpg',
            'price': 3000,
            'en_certification': 'EN_A',
            'year': '10-10-2015',
            "condition": "New",
            "test": 'Yes',
            "porosity": 300,
        }

        form = CreateWingForm(data)

        self.assertFalse(form.is_valid())

    def test_edit_form_fields_to_be_equal_to_created_wing(self):
        data = {
            'manufacturer': 'Advance',
            'model': 'Bi2',
            'image_url': 'https://ojovolador.com/wp-content/uploads/2019/07/ADVANCE_OMEGA_XALPS_HEAD.jpg',
            'price': 3000,
            'en_certification': 'EN_A',
            'year': '10-10-2015',
            "condition": "New",
            "test": 'Yes',
            "porosity": 300,
        }

        created_form = CreateWingForm(data)
        edit_form = EditWingForm(data)
        create_value = []
        edit_value = []

        for create in created_form:
            create_value.append(create.value())

        for edit in edit_form:
            edit_value.append(edit.value())

        self.assertEquals(create_value, edit_value)

    def test_edit_form_manufacturer_to_be_not_equal_to_created_wing(self):
        data = {
            'manufacturer': 'Advance',
            'model': 'Bi2',
            'image_url': 'https://ojovolador.com/wp-content/uploads/2019/07/ADVANCE_OMEGA_XALPS_HEAD.jpg',
            'price': 3000,
            'en_certification': 'EN_A',
            'year': '10-10-2015',
            "condition": "New",
            "test": 'Yes',
            "porosity": 300,
        }

        created_form = CreateWingForm(data)
        edit_form = EditWingForm(data)
        create_manufacturer = created_form["manufacturer"].value()
        edit_manufacturer = edit_form["manufacturer"].value() + "a"

        self.assertNotEqual(create_manufacturer, edit_manufacturer)

    def test_edit_form_fields_to_be_equal_to_created_harness(self):
        data = {
            'manufacturer': 'Advance',
            'model': 'Impress 2',
            'image_url': 'https://www.infinityfly.it/media/annunci/IMG-20181213-WA0008.jpg',
            'price': 400,
            'category': 'pod',
            'year': '10-10-2015',
            "condition": "New",
        }

        created_form = CreateHarnessesForm(data)
        edit_form = EditHarnessesForm(data)
        create_value = []
        edit_value = []

        for create in created_form:
            create_value.append(create.value())

        for edit in edit_form:
            edit_value.append(edit.value())

        self.assertEquals(create_value, edit_value)

    def test_edit_form_fields_to_be_equal_to_created_reserves(self):
        data = {
            'manufacturer': 'Advance',
            'model': 'SQR',
            'image_url': 'https://www.independence.aero/media/1750x960/k-30024-rs-smart-5176-q_fly-market.jpg',
            'price': 2000,
            'type': 'Light',
            'year': '10-10-2015',
            "condition": "New",
        }

        created_form = CreateReservesForm(data)
        edit_form = EditReservesForm(data)
        create_value = []
        edit_value = []

        for create in created_form:
            create_value.append(create.value())

        for edit in edit_form:
            edit_value.append(edit.value())

        self.assertEquals(create_value, edit_value)

    def test_edit_form_fields_to_be_equal_to_created_instruments(self):
        data = {
            'manufacturer': 'SysNav XL',
            'image_url': 'https://paragliding.rocktheoutdoor.com/wp-content/uploads/2021/06/vario-syride-SYSNAV-XL-5.jpg',
            'price': 550,
            'type': 'AltiVariosGPS',
            "condition": "New",
        }

        created_form = CreateInstrumentsForm(data)
        edit_form = EditInstrumentsForm(data)
        create_value = []
        edit_value = []

        for create in created_form:
            create_value.append(create.value())

        for edit in edit_form:
            edit_value.append(edit.value())

        self.assertEquals(create_value, edit_value)

    def test_edit_form_fields_to_be_equal_to_created_helmets(self):
        data = {
            'manufacturer': 'Nerv',
            'image_url': 'https://extremeuniverse.eu/wp-content/plugins/phastpress/phast.php/c2VydmljZT1pbWFnZXMmc3JjPWh0dHBzJTNBJTJGJTJGZXh0cmVtZXVuaXZlcnNlLmV1JTJGd3AtY29udGVudCUyRnVwbG9hZHMlMkYyMDIwJTJGMDElMkZOZXJ2LXJvbGJhci0wMS0zMDB4MzAwLmpwZyZjYWNoZU1hcmtlcj0xNjM4MzA0NzMzLTE1Mjc0JnRva2VuPTA3NzQ5YTlhMWYwNTA4Yzk.q.jpg',
            'price': 600,
            'visor': 'Yes',
            "condition": "New",
        }

        created_form = CreateHelmetsForm(data)
        edit_form = EditHelmetsForm(data)
        create_value = []
        edit_value = []

        for create in created_form:
            create_value.append(create.value())

        for edit in edit_form:
            edit_value.append(edit.value())

        print(create_value)
        print(edit_value)

        self.assertEquals(create_value, edit_value)
