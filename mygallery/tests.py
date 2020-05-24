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

class CategoryTestClass(TestCase):
      # Set up method
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.travel = Category.objects.create(title="Travel")

    # Testing  instance
    def test_instance(self):
       self.assertTrue(isinstance(self.travel, Category))

    # Testing Save Method
    def save_method_test(self):
        self.travel.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)


# Image
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new location and saving it
        self.kenya = Location(country = 'Tanzania')
        self.kenya.save_location()

        # Creating a new category and saving it
        self.travel = Category(name = 'Travel')
        self.travel.save()

        self.image1= Image(name = 'Lancelin', description = 'SandDunes in W.A', location = self.kenya, category = self.travel)
        self.image1.save()

 # Testing Save Method
    def save_method_test(self):
        self.image1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()
