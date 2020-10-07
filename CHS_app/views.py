from django.shortcuts import render, redirect
from CHS_app.models import Subjects, Student,Teachers, Parents, Hostel, Fee, Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib import messages


# Create your views here.

#####frontend###
def homeview(request):
    return render(request, 'frontend/common/home.html')


# def loginview(request):
#     return render(request,'frontend/common/login.html')

#
# def addtitionalinfo(request):
#     if request.method == 'POST':
#         if (request.POST.get('phone_Number') and
#                 request.POST.get('Occupation')
#         ):
#             phone = request.POST.get('Phone_Number')
#             occp = request.POST.get('Occupation')
#
#             parent = Parents()
#
#             parent.phone_Number = phone
#             parent.Occupation = occp
#             parent.save()
#             return render(request, 'frontend/common/studentdetails.html')
#         else:
#             return redirect('additionall')
#     else:
#         return redirect('additional')

def parentregistrationview(request):
    return render(request,'registration/register.html')

def parentregistration(request):
    if request.method == 'POST':
        if (request.POST.get('Parents_name') and
                request.POST.get('Email') and
                request.POST.get('phone_Number') and
                request.POST.get('Occupation')

        ):
            pname = request.POST.get('Parents_name')
            email = request.POST.get('Email')
            phone = request.POST.get('phone_Number')
            occp = request.POST.get('Occupation')

            parent = Parents()
            parent.Parents_name = pname
            parent.Email = email
            parent.phone_Number = phone
            parent.Occupation = occp

            parent.save()
            messages.success(request, 'Done!')
            return redirect('student-details')
        else:
            messages.error(request, 'Not Saved!!!')
            return redirect('registration-form')
    else:
        return redirect('registration-form')

def parentloginview(request):
    if request.method == 'POST':
        pname=request.POST['Parents_name']
        phone=request.POST['phone_Number']
        parent_exist = Parents.objects.filter(Parents_name=pname,phone_Number=phone)
        if parent_exist:
            request.session['Parents_name']=pname
            request.session['phone_Number']=phone
            messages.success(request,'Authenticated successfully')
            return redirect('profile')
        else:
            messages.error(request,'invalid login')
            return render(request,'registration/login.html')

def studentdetailsview(request):
    student = Student.objects.all()
    dict = {'student' : student}
    return render(request,'frontend/common/studentdetails.html',dict)

def studentdetails(request):
    if request.method == 'POST':
        if (request.POST.get('First_name') and
                request.POST.get('Last_name') and
                request.POST.get('Surname') and
                request.POST.get('class_form') and
                request.POST.get('DateOfBirth') and
                request.POST.get('KCPE_Marks') and
                request.POST.get('Former_school') and
                request.POST.get('Subjects_taken')
        ):
            fname = request.POST.get('First_name')
            lname = request.POST.get('Last_name')
            surname = request.POST.get('Surname')
            cform = request.POST.get('class_form')
            dob = request.POST.get('DateOfBirth')
            kcpe = request.POST.get('KCPE_Marks')
            former = request.POST.get('Former_school')
            subj = request.POST.get('Subjects_taken')

            student = Student()
            student.First_name = fname
            student.Last_name = lname
            student.Surname = surname
            student.class_form = cform
            student.DateOfBirth = dob
            student.KCPE_Marks = kcpe
            student.Former_school = former
            student.Subjects_taken = subj
            student.save()
            messages.success(request, 'submited')
            return redirect('parent-login')
        else:
            messages.error(request, 'oooops! something went wrong')
            return redirect('student-form')

    else:
        return redirect('student-form')


#####backend###
@login_required
def dashboardview(request):
    no_of_students = Student.objects.all().count()
    no_of_teachers = Teachers.objects.all().count()
    no_of_subjects = Subjects.objects.all().count()
    dict = {'no_of_students': no_of_students, 'no_of_teachers': no_of_teachers,
            'no_of_subjects': no_of_subjects}
    return render(request, 'chsapp/dashboard.html', dict)



@login_required
def nonteachingview(request):
    return render(request, 'chsapp/Non-teaching.html')


@login_required
def parentsview(request):
    parents = Parents.objects.all()
    dict = {'parents': parents}
    return render(request, 'chsapp/parents.html', dict)


@login_required
def addparentview(request):
    if request.method == 'POST':
        if (request.POST.get('Parents_name') and
                request.POST.get('Email') and
                request.POST.get('phone_Number') and
                request.POST.get('Occupation')

        ):
            pname = request.POST.get('Parents_name')
            email = request.POST.get('Email')
            phone = request.POST.get('phone_Number')
            occp = request.POST.get('Occupation')

            parent = Parents()
            parent.Parents_name = pname
            parent.Email = email
            parent.phone_Number = phone
            parent.Occupation = occp

            parent.save()
            messages.success(request, 'Done!')
            return redirect('parents')
        else:
            messages.error(request, 'Not Saved!!!')
            return redirect('parents')
    else:
        return redirect('parents')


def updateparentview(request, parent_id):
    if request.method == 'POST':
        if (request.POST.get('Parents_name') and
                request.POST.get('Email') and
                request.POST.get('phone_Number') and
                request.POST.get('Occupation')

        ):
            Parents.objects.filter(id=parent_id).update(
                pname=request.POST.get('Parents_name'),
                email=request.POST.get('Email'),
                phone=request.POST.get('phone_Number'),
                occp=request.POST.get('Occupation')
            )
            messages.success(request, 'parent updated')
            return redirect('parents')
        else:
            messages.error(request, 'error in updating parent')
            return redirect('parents')

    else:
        return redirect('parents')


def deleteparentview(request, parent_id):
    if request.method == 'POST':
        Parents.objects.filter(id=parent_id).delete()
        messages.success(request, 'parent deleted')
        return redirect('parents')
    else:
        messages.error(request, 'error in deleting parent')
        return redirect('parents')


@login_required
def studentdetailsview(request):
    students = Student.objects.all()
    dict = {'students': students}
    return render(request, 'chsapp/student.html', dict)


@login_required
def admitstudentview(request):
    if request.method == 'POST':
        if (request.POST.get('First_name') and
                request.POST.get('Last_name') and
                request.POST.get('Surname') and
                request.POST.get('class_form') and
                request.POST.get('Former_school') and
                request.POST.get('KCPE_Marks') and
                request.POST.get('DateOfBirth') and
                request.POST.get('Subjects_taken')
        ):

            fname = request.POST.get('First_name')
            lname = request.POST.get('Last_name')
            surname = request.POST.get('Surname')
            cform = request.POST.get('class_form')
            fschool = request.POST.get('Former_school')
            kmarks = request.POST.get('KCPE_Marks')
            dob = request.POST.get('DateOfBirth')
            subj = request.POST.get('Subjects_taken')

            laststudent = Student.objects.last()
            if laststudent:
                newstudent = laststudent.id + 1
            else:
                newstudent = 1
            adminno = str(0) + str(0) + str(0) + str(newstudent)

            student_instance = Student()
            student_instance.Adm_no = adminno
            student_instance.First_name = fname
            student_instance.Last_name = lname
            student_instance.Surname = surname
            student_instance.class_form = cform
            student_instance.Former_school = fschool
            student_instance.KCPE_Marks = kmarks
            student_instance.DateOfBirth = dob
            student_instance.Subjects_taken = subj
            student_instance.save()
            messages.success(request, 'student added')
            return redirect('students-admin')

        else:
            messages.error(request, 'student not added')
            return redirect('students-admin')

    else:
        return redirect('students-admin')


def updatestudentview(request, student_id):
    if request.method == 'POST':

        if (request.POST.get('First_name') and
                request.POST.get('Last_name') and
                request.POST.get('Surname') and
                request.POST.get('Parents_name') and
                request.POST.get('class_form') and
                request.POST.get('Subjects_taken')
        ):
            Student.objects.filter(id=student_id).update(
                First_name=request.POST.get('First_name'),
                Last_name=request.POST.get('Last_name'),
                Surname=request.POST.get('Surname'),
                Parent_name=request.POST.get('Parents_name'),
                Class_form=request.POST.get('class_form'),
                Subject_taken=request.POST.get('Subjects_taken')
            )
            messages.success(request, 'student saved')
            return redirect('students-admin')
        else:
            return redirect('students-admin')

    else:
        return redirect('students-admin')


def deletestudentview(request, student_id):
    if request.method == 'POST':
        Student.objects.filter(id=student_id).delete()
        messages.success(request, 'student deleted')
        return redirect('students-admin')
    else:
        messages.error(request, 'student not deleted')
        return redirect('students-admin')


@login_required
def subjectsview(request):
    subjects = Subjects.objects.all()
    dict = {'subjects': subjects}
    return render(request, 'chsapp/subjects.html', dict)


@login_required
def addsubject(request):
    if request.method == 'POST':
        if (request.POST.get('Subject_name') and
                request.POST.get('Subject_code') and
                request.POST.get('Subject_teacher')
        ):
            subjectname = request.POST.get('Subject_name')
            subjectcode = request.POST.get('Subject_code')
            subjectteacher = request.POST.get('Subject_teacher')

            subject_instance = Subjects()
            subject_instance.Subject_name = subjectname
            subject_instance.Subject_code = subjectcode
            subject_instance.Subject_teacher = subjectteacher
            subject_instance.save()
            messages.success(request, 'added successfully')
            return redirect('subjects')
        else:
            messages.warning(request, 'something is wrong')
            return redirect('subjectS')
    else:
        return redirect('subjects')


@login_required
def editsubjectview(request, subject_id):
    if request.method == 'POST':
        if (request.POST.get('Subject_name') and
                request.POST.get('Subject_code') and
                request.POST.get('Subject_teacher')
        ):
            Subjects.objects.filter(id=subject_id).update(
                Subject_name=request.POST.get('Subject_name'),
                Subject_code=request.POST.get('Subject_code'),
                Subject_teacher=request.POST.get('Subject_teacher')
            )
            messages.success(request, 'subject saved')
            return redirect('subjects')
        else:
            messages.error(request, 'try again!')
            return redirect('subjects')

    else:
        return redirect('subjects')


@login_required
def teachersview(request):
    teachers = Teachers.objects.all()
    dict = {'teachers': teachers}
    return render(request, "chsapp/Teachingstaff.html", dict)


@login_required
def addteachersview(request):
    if request.method == 'POST':
        if (request.POST.get('Tsc_no') and
                request.POST.get('First_name') and
                request.POST.get('Last_name') and
                request.POST.get('Email') and
                request.POST.get('Phone_Number')
        ):
            tscno = request.POST.get('Tsc_no')
            fname = request.POST.get('First_name')
            lname = request.POST.get('Last_name')
            email = request.POST.get('Email')
            phone = request.POST.get('Phone_Number')

            teacher = Teachers()
            teacher.Tsc_no = tscno
            teacher.First_name = fname
            teacher.Last_name = lname
            teacher.Email = email
            teacher.Phone_Number = phone
            teacher.save()
            messages.success(request, 'Teacher added')
            return redirect('teachers-admin')
        else:
            messages.error(request, 'ooops!something went wrong')
            return redirect('teachers-admin')

    else:
        return redirect('teachers-admin')


def updateteacherview(request, teacher_id):
    if request.method == 'POST':
        if (request.POST.get('Tsc_no') and
                request.POST.get('First_name') and
                request.POST.get('Last_name') and
                request.POST.get('Email') and
                request.POST.get('Phone_Number')
        ):
            Teachers.objects.filter(id=teacher_id).update(
                tscno=request.POST.get('Tsc_no'),
                fname=request.POST.get('First_name'),
                lname=request.POST.get('Last_name'),
                email=request.POST.get('Email'),
                phone=request.POST.get('Phone_Number')
            )
            messages.success(request, 'teacher updated')
            return redirect('teachers-admin')
        else:
            messages.error(request, 'teacher not addded')
            return redirect('teachers-admin')

    else:
        return redirect('teachers-admin')


@login_required
def dormsview(request):
    dorms = Hostel.objects.all()
    dict = {'dorms': dorms}
    return render(request, 'chsapp/hostels.html', dict)


@login_required
def hostelview(request):
    if request.method == 'POST':
        if (request.POST.get('name') and
                request.POST.get('dormcaptain')
        ):

            hname = request.POST.get('name')
            dcapt = request.POST.get('dormcaptain')

            hostels = Hostel()
            hostels.name = hname
            hostels.dormcaptain = dcapt
            hostels.save()
            messages.success(request, 'done!')
            return redirect('hostels')
        else:
            messages.error(request, 'try again!')
            return redirect('hostels')
    else:
        return redirect('hostels')


def updatehostel(request, hostel_id):
    if request.method == 'POST':
        if (request.POST.get('name') and
                request.POST.get('dormcaptain')):

            Hostel.objects.filter(id=hostel_id).update(
                name=request.POST.get('name'),
                dormcaptain=request.POST.get('dormcaptain')
            )
            messages.success(request, 'updated')
            return redirect('hostels')
        else:
            messages.error(request, 'not updated')
            return redirect('hostels')
    else:
        return redirect('hostels')


def deletehostel(request, hostel_id):
    if request.method == 'POST':
        Hostel.objects.filter(id=hostel_id).delete()
        messages.success(request, 'hostel deleted')
        return redirect('hostels')
    else:
        messages.error(request, 'hostel not deleted')
        return redirect('hostels')


def feeview(request):
    return render(request, 'chsapp/fee.html')


def schoolfeesviews(request):
    if request.method == 'POST':
        if (request.POST.get('term') and
                request.POST.get('amount')):

            trm = request.POST.get('term')
            amnt = request.POST.get('amount')

            fee = Fee()
            fee.term = trm
            fee.amount = amnt
            fee.save()
            messages.success(request, 'fee saved')
            return redirect('fees')
        else:
            messages.error(request, 'fee not saved')
            return redirect('fees')

    else:
        return redirect('fees')


def updatefeeview(request, fee_id):
    if request.method == 'POST':
        if (request.POST.get('term') and
                request.POST.get('amount')):

            Fee.objects.filter(id=fee_id).updaate(
                request.POST.get('term') and
                request.POST.get('amount')
            )
            messages.success(request, 'fee updated')
            return redirect('fees')
        else:
            messages.error(request, 'error in updating fee!')

    else:
        return redirect('fees')


def deletefeeview(request, fee_id):
    if request.method == 'POST':
        Fee.objects.filter(id=fee_id).delete()
        messages.success(request, 'fee dleted')
        return redirect('fees')
    else:
        messages.error(request, 'not deleted!')
        return redirect('fees')


######admn check in####


def admin_check_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'logged in')
            return redirect('dashboard-admin')
        else:
            messages.warning(request, 'invalid login')
            return render(request, 'registration/adminlogin.html')


    else:
        return render(request, 'registration/adminlogin.html')


def admin_check_out(request):
    logout(request)
    messages.warning(request, 'loggedout')
    return render(request, 'registration/adminlogin.html')


#############
def parent_check_out(request):
    logout(request)
    messages.warning(request, 'loggedout')
    return render(request, 'registration/login.html')


@login_required
def profile(request):
    messages.success(request, 'hae!how is you?')
    return render(request, 'proapp/stddashboard.html')
