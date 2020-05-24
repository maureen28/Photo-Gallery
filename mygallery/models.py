from django.db import models

# Create your models here.

class Location(models.Model):
    country = models.CharField(max_length =150)

    def __str__(self):
        return self.country

    def save_location(self):
         self.save()

    class Meta:
        ordering = ['country']

class Category(models.Model):
    title = models.CharField(max_length = 100, unique=True)

    def __str__(self):
            return self.title

    def save_category(self):
        self.save()

class Image(models.Model):
    name = models.CharField(max_length = 80)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    #  Save image
    def save_image(self):
        self.save()

    # Delete image
    def delete_image(self):
        self.delete()

    #  Update image
    @classmethod
    def update_image(cls,current_value,new_value):
        filtered_image = Image.objects.filter(image_name=current_value).update(image_name=new_value)
        return filtered_image

    #  get image by id image
    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result

    # search by category
    @classmethod
    def search_by_category(cls,search_term):
        search_result = cls.objects.filter(image_category__cat_name__icontains=search_term)
        return search_result

    # filter by location
    @classmethod
    def filter_by_location(cls,location):
        filtered_result = cls.objects.filter(image_location__location_name__icontains=location)
        return filtered_result

    # all images
    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item;
