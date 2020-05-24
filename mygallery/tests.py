from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class LocationTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.kenya = Location.objects.create(country="Tanzania")

    # Testing  instance
    def test_instance(self):
       self.assertTrue(isinstance(self.kenya, Location))


    # Testing Save Method
    def save_method_test(self):
        self.kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

