from django.shortcuts import render,redirect

from .models import Doctor, Patient

# Create your views here.
def homePageView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username == 'admin' and password == 'admin':
            return render(request, 'admin.html')
        elif Doctor.objects.filter(username=username, password=password).exists():
            patients = Patient.objects.all().filter(doctorname=username)
            return render(request, 'doctor.html', {'patients': patients})
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
        doctorname = request.POST['doctorname']
        patient = Patient(
            name=name, 
            email=email, 
            mobile=mobile, 
            address=address,
            doctorname=doctorname) 
        
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



def singlePatientView(request,patient_id):
  patient = Patient.objects.get(pk = patient_id)
  context = {
        'patient':patient
  }  
  return render(request=request,template_name='singlepatient.html',context=context)

def updatePatientView(request, patient_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        doctorname = request.POST['doctorname']

        # Print the values for debugging.
        print("Name:", name)
        print("Email:", email)
        print("Mobile:", mobile)
        print("Address:", address)
        print("Doctor Name:", doctorname)

        patient = Patient.objects.get(pk=patient_id)
        patient.name = name
        patient.email = email
        patient.mobile = mobile
        patient.address = address
        patient.doctorname = doctorname
        patient.save()
    return redirect('listPatient')  

def consult(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    print("tesing")
    if request.method == 'POST':
        consultation = request.POST['consultation']
        patient.consultation = consultation
        patient.save()
        patients = Patient.objects.all().filter(doctorname=patient.doctorname)
        return render(request, 'doctor.html', {'patients': patients})
    return render(request, 'consult.html', {'patient': patient})