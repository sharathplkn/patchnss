from django.shortcuts import render
from django.http import HttpResponse
from .models import volunteer
from .models import Department,Attendance,Event
from django.db import connection
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def ns(request):
    return render(request,'nss/home.html')
@login_required()
def add_volunteer(request):
    if request.method=="POST" and request.FILES:
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
        image=request.FILES.get ('image')
        voluntee=volunteer(image=image,name=name,guard_name=guard_name,guard_mob_no=guard_mob_no,sex=sex,dob=dob,department=department,year=year,community=community,address=address,blood_group=blood_group,height=height,weight=weight,mobile_no=mobile_no,Email_id=Email_id,year_of_enrollment=year_of_enrollment,cultural_talents=cultural_talents,hobbies=hobbies,roll_no=roll_no)
        voluntee.save()
        dep=Department(dep_name=department,roll_no=roll_no,name=name)
        dep.save()
        return HttpResponse('submitted')
    return render(request,'nss/form.html')
@login_required()
def view_volunteer(request):
    vol={
        'volunteer':volunteer.objects.all()
    }
    return render(request,'nss/view_volunteer.html',vol)
@login_required()
def attendance(request):
    vole = {
        'vol': volunteer.objects.all()
    }
    eve = {
        'even': Event.objects.all().order_by('date').values()
    }

    if request.method == "POST":
        datet = request.POST.get('date')
        name_list = request.POST.getlist('name')
        event=request.POST.get('event')
        time=request.POST.get('time')
        #converting roll_numbers from string to Integers

        for name_department in name_list:
            # Split the value into roll_no and department_name
            name, department_name = name_department.split('_')

            # Convert roll_no to an integer
            volunteer_instance= volunteer.objects.get(name=name)
            # Save the attendance record
            att = Attendance(vol_id=volunteer_instance,date=datet, name=name, department=department_name,event=event)
            att.save()

        return HttpResponse("Attendance Submitted")

    return render(request, 'nss/attendance.html',{**vole,**eve})
@login_required()
def view_attendance(request):
    at={
        'atte':Attendance.objects.all().order_by('date','department').values()
    }
    return render(request,'nss/view_attendance.html',at)
@login_required()
def view_attendance2(request):
    eve = {
        'even': Event.objects.all().order_by('date').values()
    }
    if request.method == "POST":
        ev = request.POST.get('event')
        selected_event=ev
        res = {
            'resul': Attendance.objects.filter(event=ev).order_by('date').values()
        }
        return render(request, 'nss/sample.html',{**res,**eve,'selected_event': selected_event})
    return render(request,'nss/sample.html',eve)
@login_required()
def volunteer_details(request, volunteer_name):
    # Assuming you have a Volunteer model with a 'name' field
    vol={
        'voluntee':volunteer.objects.filter(volunteer_id=volunteer_name)
    }
    
    ev={
        'even':Attendance.objects.filter(vol_id=volunteer_name)
    }
    # Pass the volunteer details to the template
    return render(request, 'nss/volunteer_details.html', {**vol,**ev})
@login_required()
def add_event(request):
    if request.method=="POST" and request.FILES:
        event_name=request.POST.get('event_name')
        date=request.POST.get('date')
        start_time=request.POST.get('start_time')
        end_time=request.POST.get('end_time')
        photo=request.FILES.get('photo')
        des=request.POST.get('des')
        ev=Event(des=des,event_name=event_name,date=date,start_time=start_time,end_time=end_time,photo=photo)
        ev.save()
        return HttpResponse('submitted')
    return render(request,'nss/add_event.html')

@login_required()
def report(request):
    report={
        'event':Event.objects.all()
    }
    return render(request,'nss/report.html',report)