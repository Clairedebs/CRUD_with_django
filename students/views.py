from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.utils.text import slugify
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib import messages
# Create your views here.
# View all student
def home(request):
    students = Student.objects.order_by('firstname')
    return render(request, "students/home.html",context={"students":students})

    
def student_details(request,slug):
    student = get_object_or_404(Student, slug=slug)
    return render(request, "",context={"student":student})

# Add a student
def add_student(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dateNais = request.POST.get('dateNais')
        sexe = request.POST.get('sexe')
        level = request.POST.get('level')
        
        Student.objects.create(
            firstname=firstname,
            lastname=lastname,
            dateNais=dateNais,
            sexe=sexe,
            level=level,
        )
        messages.success(request, 'Student added successfully!')
        return redirect('home')
    
    return render(request, "students/form.html")

# Delete a student
def delete_students(request,slug):
    student = get_object_or_404(Student,slug=slug)
    student.delete()
    messages.success(request, 'Student deleted successfully!')
    return redirect('home')

# Update a student 
def update_students(request,slug):
    s = get_object_or_404(Student,slug=slug)
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dateNais = request.POST.get('dateNais')
        sexe = request.POST.get('sexe')
        level = request.POST.get('level')
        s.firstname = firstname
        s.lastname = lastname
        s.dateNais = dateNais
        s.sexe = sexe
        s.level = level
        s.save()
        messages.success(request, 'Student update successfully!')
        return redirect('home')
    
    return render(request, "students/update.html",context={"student":s})