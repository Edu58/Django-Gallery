from django.test import TestCase
from .models import Categories, Locations, Images


# Create your tests here.
class TestCategories(TestCase):
    def setUp(self) -> None:
        self.example_category = Categories(name="New Category")

    def test_category_instance(self):
        self.assertTrue(isinstance(self.example_category, Categories))
