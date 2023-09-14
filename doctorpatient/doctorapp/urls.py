from django.urls import path
from . import views


urlpatterns=[
  path(route='', view=views.homePageView, name='login'),
  path(route='doctor/', view=views.doctorPageView, name='doctor'),
  path(route="admin/", view=views.adminPageView, name="admin"),

  path(route="addPatient/", view=views.addPatientPageView, name="addPatient"),
  path(route="addDoctor/", view=views.addDoctorPageView, name="addDoctor"),
  path(route="listPatient/", view=views.listPatientPageView, name="listPatient"),
  path(route="listDoctor/", view=views.listDoctorPageView, name="listDoctor"),

   path(route='<int:patient_id>/',view = views.singlePatientView, name='getsinglepatient'),
   path(route='update/<int:patient_id>/',view = views.updatePatientView, name='updatepatient'),
   path(route='delete/<int:patient_id>/',view = views.deletePatientView, name='deletepatient'),

   
   path(route='doctor<int:doctor_id>/',view = views.singleDoctorView, name='getsingledoctor'),
 
  path(route='update/doctor<int:doctor_id>/',view = views.updateDoctorView, name='updatedoctor'),
   
   path(route='consult/<int:patient_id>/',view = views.consult, name='consult'),
]