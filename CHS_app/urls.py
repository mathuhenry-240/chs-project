from django.urls import path
from CHS_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('registration/form/',views.parentregistrationview,name='registration-form'),
    path('register/', views.parentregistration, name='register'),
    path('parent/login/',views.parentloginview,name='parent-login'),
    path('student/form/',views.studentdetailsview,name='student-form'),
    path('studentdetails/', views.studentdetails, name='student-details'),
    path('profile', views.profile, name='profile'),
    path('adminlogin/', views.admin_check_in, name='admin-login'),
    path('adminlogout/', views.admin_check_out, name='admin-logout'),
    path('parentlogout/', views.parent_check_out, name='parent-logout'),
    path('hostel/dorms/', views.dormsview, name='hostel-dorms'),
    path('hostels/', views.hostelview, name='hostels'),

    # path('profile',views.profile,name='profile'),

    ####backend
    path('dashboard/admin/', views.dashboardview, name='dashboard-admin'),
    path('nonteaching/', views.nonteachingview, name='nonteaching'),
    path('parents/', views.parentsview, name='parents'),
    path('students/admin/', views.studentdetailsview, name='students-admin'),
    path('teachers/admin/', views.teachersview, name='teachers-admin'),
    path('subjects/', views.subjectsview, name='subjects'),
    path('student/admit/', views.admitstudentview, name='admit-student'),
    path('subject/add/', views.addsubject, name='add-subject'),
    path('parent/add/', views.addparentview, name='add-parents'),
    path('parent/update/<int:parent_id>/',views.updateparentview,name='update-parent'),
    path('parent/delete/<int:parent_id>/',views.deleteparentview,name='delete-parent'),
    path('teachers/add/', views.addteachersview, name='add-teachers'),
    path('student/update/<int:student_id>/', views.editsubjectview, name='update-student'),
    path('student/delete/<int:student_id>/', views.deletestudentview, name='delete-student'),
    path('subject/update/<int:subject_id>/', views.editsubjectview, name='update-subject'),
    path('hostel/update/<int:hostel_id>/', views.updatehostel, name='update-hostel'),
    path('hostel/delete/<int:hostel_id>/', views.deletehostel, name='delete-hostel'),
    path('teacher/update/<int:teacher_id>/',views.updateteacherview,name='update-teacher'),
    path('add/fees/',views.schoolfeesviews,name='add-fees'),
    path('fees/',views.feeview,name='fees'),
    path('fees/update/<int:fee_id>/',views.updatefeeview,name='update-fee'),
    path('fees/delete/<int:fee_id>/',views.deletefeeview,name='delete-fee'),

]
