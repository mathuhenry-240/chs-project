from django.shortcuts import render, redirect
from CHS_app.models import Subjects, Student, Parents,Hostel,Fee,Event
from django.contrib import messages

# Create your views here.
def dashboardview(request):
    return render(request, 'proapp/stddashboard.html')


def dormhostelsview(request):
    dorm=Hostel.objects.all()
    dict = {'dorm' : dorm}
    return render(request,'proapp/dorm.html',dict)




def eventsview(request):
    return render(request, 'proapp/events.html')


def feeview(request):
    fees=Fee.objects.all()
    dict={'fees' : fees}
    return render(request, 'proapp/fee.html',dict)


def subjectview(request):
    subjects = Subjects.objects.all()
    dict = {'subjects': subjects}
    return render(request, 'proapp/subject.html', dict)


def studentview(request):
    Students = Student.objects.all()
    dict = {'Students': Students}
    return render(request, 'proapp/registration.html',dict)


# def updatestudentiew(request,student_id):
#     students = Student.objects.filter(id=student_id).all()
#     dict = {'students' : students}
#     return redirect('students-admin')
