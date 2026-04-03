from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student

def login_view(request):
    error = ''
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
        error = 'Invalid credentials'
    return render(request, 'App1/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    students = Student.objects.all()
    return render(request, 'App1/home.html', {'students': students})

@login_required(login_url='login')
def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            age=request.POST['age'],
            course=request.POST['course'],
        )
    return redirect('home')

@login_required(login_url='login')
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()
        return redirect('home')
    return render(request, 'App1/edit.html', {'student': student})

@login_required(login_url='login')
def delete_student(request, pk):
    get_object_or_404(Student, pk=pk).delete()
    return redirect('home')