from django.urls import path
from profileapp import views

urlpatterns = [
    path('dashboard/parent/', views.dashboardview, name='dashboard-parent'),
    path('fee/structure/', views.feeview, name='fee-structure'),
    path('events/', views.eventsview, name='events'),
    path('hostels/dorms', views.dormhostelsview, name='hostels-dorms'),
    path('subjects/student/', views.subjectview, name='subjects-student'),
    path('students/parent/', views.studentview, name='students-parent'),
    # path('student/update/',views.updatestudentview,name='update-student'),
]
