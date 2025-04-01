from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Student(models.Model):
    
    firstname = models.CharField(max_length=100, blank=False, null=False)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    dateNais = models.DateField(blank=False)
    sexe = models.CharField(max_length=1, blank=False, null=False)
    level = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,max_length=255,null=False,blank=True)
    
    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.firstname

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.firstname)
            self.slug = base_slug
            counter = 1
            while Student.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)