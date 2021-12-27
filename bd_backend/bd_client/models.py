from django.db import models

# Create your models here.

class Firstname(models.Model):
    firstname = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return "%s" % (self.firstname)

class Lastname(models.Model):
    lastname = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return "%s" % (self.lastname)

class Surname(models.Model):
    surname = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return "%s" % (self.surname)

class Persons(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.ForeignKey(Firstname, related_name='_firstname', on_delete=models.CASCADE)
    lastname = models.ForeignKey(Lastname, related_name='_lastname', on_delete=models.CASCADE)
    surname = models.ForeignKey(Surname, related_name='_surname', on_delete=models.CASCADE)
    email = models.CharField(max_length = 100)
    telephone = models.CharField(max_length = 15)
    address = models.CharField(max_length = 150)