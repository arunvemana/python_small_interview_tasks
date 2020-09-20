from django.db import models

# Create your models here.

# used recursive realtionship.

class EmployeeManager(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', null=True,
     on_delete=models.SET_NULL, default=None, related_name='manger_name')

    def __str__(self):
        return self.first_name + ' ' +self.last_name

    # used for the jsonresponse to get the query string object of foreign class as str.
    def __repr__(self):
        return self.__str__()