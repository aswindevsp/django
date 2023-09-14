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
]