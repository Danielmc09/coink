from django.test import TestCase
from .models import RegisterUser

# Create your tests here.

class AuthorModelTest(TestCase):
    
    """
    It creates a test user in the database
    :param cls: This is the class that is being set up
    """
    @classmethod
    def setUpTestData(cls):
        RegisterUser.objects.create(
            full_name='test',
            email='test@test.co',
            city='test'
        )

    def test_full_name(self):
        """
        The function tests that the full_name field label is equal to 'full name'
        """
        full_name = RegisterUser.objects.get(id=1)
        field_label = full_name._meta.get_field('full_name').verbose_name
        self.assertEquals(field_label, 'full name')

    def test_full_name_length(self):
        """
        It tests the max length of the full_name field in the RegisterUser model.
        """
        full_name = RegisterUser.objects.get(id=1)
        max_length = full_name._meta.get_field('full_name').max_length
        self.assertEquals(max_length, 100)

    def test_email(self):
        """
        The above function tests the email field in the RegisterUser model.
        """
        email = RegisterUser.objects.get(id=1)
        field_label = email._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_city(self):
        """
        It tests the city field in the RegisterUser model.
        """
        city = RegisterUser.objects.get(id=1)
        field_label = city._meta.get_field('city').verbose_name
        self.assertEquals(field_label, 'city')
