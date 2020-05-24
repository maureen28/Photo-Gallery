from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setup(self):
        self.maureen = Location(country = 'Kenya')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.maureen, Location))
