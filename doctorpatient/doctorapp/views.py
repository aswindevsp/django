from django.shortcuts import render

from .models import Doctor, Patient

# Create your views here.
def homePageView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username == 'admin' and password == 'admin':
            return render(request, 'admin.html')
        elif Doctor.objects.filter(username=username, password=password).exists():
            return render(request, 'doctor.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    

def doctorPageView(request):
    return render(request, 'doctor.html')

def adminPageView(request):
    return render(request, 'admin.html')

def addPatientPageView(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        patient = Patient(
            name=name, 
            email=email, 
            mobile=mobile, 
            address=address) 
        
        patient.save()
    return render(request, 'addPatient.html')

def addDoctorPageView(request):
    print("working? ")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        speciality = request.POST['speciality']
        experience = request.POST['experience']
        qualification = request.POST['qualification']
        doctor = Doctor(
            username=username, 
            password=password, 
            name=name, 
            email=email, 
            mobile=mobile, 
            speciality=speciality, 
            experience=experience, 
            qualification=qualification)
        
        doctor.save()
    return render(request, 'addDoctor.html')

def listPatientPageView(request):
    patients = Patient.objects.all()
    return render(request, 'listPatient.html', {'patients': patients})

def listDoctorPageView(request):
    docotors = Doctor.objects.all()
    return render(request, 'listDoctor.html', {'doctors': docotors})


