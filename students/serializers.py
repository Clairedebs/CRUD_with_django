from rest_framework import serializers
from .models import Student

class StudentsSer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Student
        fields = ['firstname','lastname','dateNais','sexe','level']