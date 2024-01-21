from django.contrib import admin
from .models import volunteer,Department,Attendance
# Register your models here.
admin.site.register(volunteer)
admin.site.register(Department)
admin.site.register(Attendance)