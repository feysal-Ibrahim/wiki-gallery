from django.test import TestCase
from .models import Location , Category , Image
import datetime as dt


# Create your tests here.
class LocationTestClass ( TestCase ):
    def setUp(self):
        self.location=Location ( name="Arusha" )

    # Testing  instance for location class
    def test_instance(self):
        self.assertTrue ( isinstance ( self.location , Location ) )

    def test_save_method(self):
        self.location.save_locations ( )
        locations=Location.objects.all ( )
        self.assertTrue ( len ( locations ) > 0 )
    #
    # def test_update_location(self):
    #     new_location_name = 'Arusha,'
    #     self.location.name(self.location.name,new_location_name)
    #     changed_location = Location.objects.filter(name='Arusha')
    #     self.assertTrue(len(changed_location)>0)

    def test_delete_method(self):
        self.location.save_locations ( )
        self.location.delete_locations ( )
        locations=Location.objects.all ( )
        self.assertTrue ( len ( locations ) == 0 )


class CategoryTestClass ( TestCase ):
    def setUp(self):
        self.category=Category ( name=" ngori" )

    # Testing  instance for category class
    def test_instance(self):
        self.assertTrue ( isinstance ( self.category , Category ) )

        # Testing Save Method for category class

    def test_save_method(self):
        self.category.save_category ( )
        categories=Category.objects.all ( )
        self.assertTrue ( len ( categories ) > 0 )

        # Testing Save Method

    def test_delete_method(self):
        self.category.save_category ( )
        self.category.delete_category ( )
        categories=Category.objects.all ( )
        self.assertTrue ( len ( categories ) == 0 )


class ImageTestClass ( TestCase ):
    def setUp(self):
        # Creating a new location  and saving it
        self.location=Location ( name='Arusha' )
        self.location.save_locations ( )

        # Creating a new category and saving it
        self.category=Category ( name='ngori' )
        self.category.save_category ( )

        self.image=Image ( image="testImage" , image_url="testImageurl" , image_name="Test" ,
                           description="This is a test" , location=self.location , category=self.category )
        self.image.save ( )
        # self.image.category.add ( self.category )

    def test_instance(self):
        self.assertTrue ( isinstance ( self.image , Image ) )

    def test_saving_image(self):
        self.image.save_image ( )
        images=Image.objects.all ( )
        self.assertTrue ( len ( images ) > 0 )


    # def test_get_image_by_id(self):
    #     found_img = self.image.get_image_by_id(self.image.id)
    #     img = Image.objects.filter(id=self.image.id)
    #     self.assertTrue(found_img,img)
    #
    # def test_search_image_by_category(self):
    #     category = 1
    #     found_img = self.image.search_image(category)
    #     self.assertTrue(len(found_img)>0)

    # def test_search_image_by_location(self):
    #     location = 1
    #     found_img = self.image.filter_by_location(location)
    #     self.assertTrue(len(found_img)>1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()