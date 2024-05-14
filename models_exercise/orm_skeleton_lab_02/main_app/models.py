from django.db import models


class Employee(models.Model):
    NAME_MAX_LENGTH = 30

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Employee {self.name}, Email: {self.email_address}, created_on: {self.created_on}'


# class Department(models.Model):
#     CODE_MAX_LENGTH = 4
#     NAME_MAX_LENGTH = 50
#     LOCATION_MAX_LENGTH = 20
#     LOCATION_CHOICES = [
#         'Sofia',
#         'Plovdiv',
#         'Burgas',
#         'Varna'
#     ]
#
#     code = models.CharField(
#         max_length=CODE_MAX_LENGTH,
#         primary_key=True
#     )
#     name = models.CharField(
#         max_length=NAME_MAX_LENGTH,
#         unique=True
#     )
#     employees_count = models.PositiveIntegerField(
#         default=1,
#         verbose_name='Employees Count'
#     )
#     location = models.CharField(
#         max_length=LOCATION_MAX_LENGTH,
#         null=True,
#         choices=LOCATION_CHOICES
#         #  Holds predefined choices of each city name: "Sofia", "Plovdiv", "Burgas", "Varna"
#     )
#     last_edited_on = models.DateTimeField(
#         auto_now=True
#         #  It should not be editable.
#     )
