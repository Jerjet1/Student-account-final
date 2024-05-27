from django.shortcuts import render, redirect
from .models import StudentData
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def studentadd(request):
    students = StudentData()

    if request.method == "POST":
        students.first_name = request.POST.get('fname').capitalize()
        students.last_name = request.POST.get('lname').capitalize()
        students.age = request.POST.get('age')
        students.birthday = request.POST.get('birthday')
        students.email = request.POST.get('email')
        students.contact_no = request.POST.get('contactNo')
        students.year = request.POST.get('year')
        students.course = request.POST.get('course')

        if len(students.contact_no) > 11:
            messages.error(request, 'contact number exceed 11 digit')
        else:
            name_exist = len(StudentData.objects.filter(last_name = students.last_name, first_name = students.first_name))
            email_exist = len(StudentData.objects.filter(email = students.email))

            if name_exist > 0 and email_exist > 0:
                messages.error(request, 'name or email already exist')
            else:
                messages.success(request, 'Account successfully added')
                students.save()
    return render(request, 'homepage.html')

def searchStudent(request):
    students = StudentData.objects.all()

    if students == 0:
        messages.warning(request, 'No data available')

    if request.method == 'GET':
        search_query = request.GET.get('search', '')

        students = StudentData.objects.filter(
             Q(id__icontains = search_query)
             |Q(first_name__icontains = search_query)
             |Q(last_name__icontains = search_query)
        )
        if not students.exists():
            messages.info(request, 'No Student Found')
        else:
            return render(request, 'Search.html', {"students": students})
    return render(request, 'Search.html', {"students": students})
        