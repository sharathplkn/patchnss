from django.shortcuts import render
from django.http import HttpResponse
from .models import volunteer
from .models import Department,Attendance
# Create your views here.
def ns(request):
    return render(request,'nss/home.html')

def add_volunteer(request):
    if request.method=="POST":
        name=request.POST.get('name')
        guard_name=request.POST.get('guard_name')
        guard_mob_no=request.POST.get('guard_mob_no')
        sex=request.POST.get('sex')
        dob=request.POST.get('dob')
        department=request.POST.get('department')
        year=request.POST.get('year')
        community=request.POST.get('community')
        address=request.POST.get('address')
        blood_group=request.POST.get('blood_group')
        height=request.POST.get('height')
        weight=request.POST.get('weight')
        mobile_no=request.POST.get('mobile_no')
        Email_id=request.POST.get('Email_id')
        year_of_enrollment=request.POST.get('year_of_enrollment')
        cultural_talents=request.POST.get('cultural_talents')
        hobbies=request.POST.get('hobbies')
        roll_no=request.POST.get('roll_no')
        voluntee=volunteer(name=name,guard_name=guard_name,guard_mob_no=guard_mob_no,sex=sex,dob=dob,department=department,year=year,community=community,address=address,blood_group=blood_group,height=height,weight=weight,mobile_no=mobile_no,Email_id=Email_id,year_of_enrollment=year_of_enrollment,cultural_talents=cultural_talents,hobbies=hobbies,roll_no=roll_no)
        voluntee.save()
        dep=Department(dep_name=department,roll_no=roll_no,name=name)
        dep.save()
        return HttpResponse('submitted')
    return render(request,'nss/form.html')

def view_volunteer(request):
    vol={
        'volunteer':volunteer.objects.all()
    }
    return render(request,'nss/view_volunteer.html',vol)
    
def attendance(request):
    rol = {
        'roll': Department.objects.all()
    }

    if request.method == "POST":
        datet = request.POST.get('date')
        name_list = request.POST.getlist('name')
        event=request.POST.get('event')
        #converting roll_numbers from string to Integers
        for name_department in name_list:
            # Split the value into roll_no and department_name
            name, department_name = name_department.split('_')

            # Convert roll_no to an integer

            # Save the attendance record
            att = Attendance(date=datet, name=name, department=department_name,event=event)
            att.save()

        return HttpResponse("Attendance Submitted")

    return render(request, 'nss/attendance.html', rol)

def view_attendance(request):
    at={
        'atte':Attendance.objects.all().order_by('department').values()
    }
    return render(request,'nss/view_attendance.html',at)