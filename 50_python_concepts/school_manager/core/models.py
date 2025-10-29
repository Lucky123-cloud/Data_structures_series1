from django.db import models

# ---------- ABSTRACT BASE MODEL ----------
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        abstract = True  # ✅ Tells Django not to create a table for Person

    # ENCAPSULATION (private variable)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__secret_code = "XYZ123"  # private

    # Getter and Setter
    def get_secret_code(self):
        return self.__secret_code

    def set_secret_code(self, code):
        self.__secret_code = code

    # “Abstract-like” method (raise error if not overridden)
    def introduce(self):
        raise NotImplementedError("Subclasses must implement introduce()")


# ---------- INHERITANCE + POLYMORPHISM ----------
class Student(Person):
    grade = models.CharField(max_length=10)

    def introduce(self):
        return f"I am {self.name}, a student in grade {self.grade}."


class Teacher(Person):
    subject = models.CharField(max_length=50)

    def introduce(self):
        return f"I am {self.name}, and I teach {self.subject}."
