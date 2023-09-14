from django.shortcuts import render

# Create your views here.
def homePageView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'doctor' and password == 'doctor':
            return render(request, 'doctor.html')
        elif username == 'admin' and password == 'admin':
            return render(request, 'admin.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    

def doctorPageView(request):
    return render(request, 'doctor.html')

def adminPageView(request):
    return render(request, 'admin.html')

def addPatientPageView(request):
    return render(request, 'addPatient.html')

def addDoctorPageView(request):
    return render(request, 'addDoctor.html')

def listPatientPageView(request):
    return render(request, 'listPatient.html')

def listDoctorPageView(request):
    return render(request, 'listDoctor.html')


