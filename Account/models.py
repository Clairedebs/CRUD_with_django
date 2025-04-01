from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Person(User):
    def __str__(self):
        return f"{self.username}"
    