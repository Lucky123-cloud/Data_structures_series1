from django.db import models
from abc import ABC, abstractmethod

# Create your models here.

class Person(models.Model, ABC):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        abstract = True  # This model will not create a database table


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__secret_code = "XYZ123"  # Private attribute


    def get_secret_code(self):
        return self.__secret_code
    

    def set_secret_code(self, code):
        self.__secret_code = code


    @abstractmethod
    def introduce(self):
        pass



# INHERITANCE
class Student(Person):
    grade = models.CharField(max_length=10)

    # POLYMORPHISM - Overriding the introduce method
    def introduce(self):
        return f"Hi, I'm {self.name}, a student in grade {self.grade}."
    

class Teacher(Person):
    subject = models.CharField(max_length=100)

    # POLYMORPHISM - Overriding the introduce method
    def introduce(self):
        return f"Hello, I'm {self.name}, and I teach {self.subject}."
