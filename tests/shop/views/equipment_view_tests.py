from django.test import TestCase, Client
from django.urls import reverse


class EquipmentViewTest(TestCase):
    def setUp(self):
        self.test_profile = Client()
        self.index = reverse('index')

    def test_client_view_successfully(self):
        response = self.test_profile.get("")
        self.assertTemplateUsed(response, "index.html")

    def test_project_index_GET(self):
        response = self.test_profile.get(self.index)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_project_wings_GET(self):
        details = reverse('wings')
        response = self.test_profile.get(details)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "equipments/wings.html")

    def test_project_wings_with_wrong_url_GET(self):
        details = reverse('wings')
        response = self.test_profile.get(details)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, "equipments/wingsvvv.html")

    def test_project_harness_GET(self):
        details = reverse('harnesses')
        response = self.test_profile.get(details)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "equipments/harness.html")

    def test_project_harness_with_wrong_url_GET(self):
        details = reverse('harnesses')
        response = self.test_profile.get(details)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, "equipments/harnessvvv.html")

    def test_project_reserves_GET(self):
        details = reverse('reserves')
        response = self.test_profile.get(details)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "equipments/reserves.html")

    def test_project_reserves_with_wrong_url_GET(self):
        details = reverse('reserves')
        response = self.test_profile.get(details)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, "equipments/reservesvvv.html")

    def test_project_instruments_GET(self):
        details = reverse('instruments')
        response = self.test_profile.get(details)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "equipments/instruments.html")

    def test_project_instruments_with_wrong_url_GET(self):
        details = reverse('instruments')
        response = self.test_profile.get(details)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, "equipments/instrumentsvvv.html")

    def test_project_helmets_GET(self):
        details = reverse('helmets')
        response = self.test_profile.get(details)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "equipments/helmets.html")

    def test_project_helmets_with_wrong_url_GET(self):
        details = reverse('helmets')
        response = self.test_profile.get(details)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, "equipments/helmetsvvv.html")
