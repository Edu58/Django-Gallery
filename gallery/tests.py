from django.test import TestCase
from .models import Categories, Locations, Images


# Create your tests here.
class TestCategories(TestCase):
    def setUp(self) -> None:
        self.example_category = Categories(name="New Category")

    def test_category_instance(self):
        self.assertTrue(isinstance(self.example_category, Categories))


class TestLocations(TestCase):
    def setUp(self) -> None:
        self.example_location = Locations(name="Kenya")

    def test_location_instance(self):
        self.assertTrue(isinstance(self.example_location, Locations))


class TestImages(TestCase):
    def setUp(self) -> None:
        self.example_category = Categories(name="New Category")
        self.example_location = Locations(name="Kenya")
        self.example_image = Images(name="test image", description="This is a test for the Image model",
                                    location=self.example_location, category=self.example_category,
                                    image="../media/images/MG_1684.jpg")

    def tearDown(self) -> None:
        Categories.objects.all().delete()
        Locations.objects.all().delete()
        Images.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.example_image, Images))
