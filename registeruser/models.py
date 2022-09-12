from django.db import models

# Create your models here.

# The RegisterUser class inherits from the models.Model class, which is a class that comes from the
# django.db.models module. 
# 
# The RegisterUser class has three attributes: full_name, email, and city. 
# 
# The full_name attribute is a CharField, which means it's a string. The max_length parameter is
# required for CharFields. 
# 
# The email and city attributes are also CharFields. 
# 
# The Meta class is used to specify metadata for the RegisterUser class. In this case, we're
# specifying the name of the database table that will be used to store the data for the RegisterUser
# class. 
# 
# The __str__ method is used to specify how the RegisterUser class will be displayed when it's
# printed.

class RegisterUser(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    class Meta:
        db_table = 'register_user'

    def __str__(self):
        return self.full_name