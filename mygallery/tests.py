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

# CAREGORY TEST

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

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    # Testing Save Method
    def save_method_test(self):
        self.image1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Testing Delete Method
    def delete_method_test(self):
        self.image1.save_image()
        filtered_img = Image.objects.filter(name='Lancelin')
        Image.delete_image(filtered_img)
        final_images = Image.objects.all()
        self.assertTrue(len(final_images) == 0)

    # Testing Update Method
    def update_method_test(self):
        self.image1.save_image()
        filtered_img = Image.update_image('Lancelin','Dunes')
        fetched = Image.objects.get(name='Dunes')
        self.assertEqual(fetched.name,'Dunes')

    # Testing get image Method
    def get_image_by_id_test_method(self):
        self.image1.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)

    # Testing search image Method
    def search_by_category_test_method(self):
        self.image1.save_image()
        fetch_specific = Category.objects.get(title='Food')
        self.assertTrue(fetch_specific.title=='Food')


    # Testing filter location Method
    def filter_by_location_test_method(self):
        self.image1.save_image()
        fetch_specific = Location.objects.get(country='Tanzania')
        self.assertTrue(fetch_specific.country=='Tanzania')

    #  test all images
    def display_all_images_test_method(self):
        self.image1.save_image()
        final_images = Image.retrieve_all()
        self.assertEqual(final_images.name,'Lancelin')

