from django.contrib import admin
from .models import Employee,Student_pinfo,Student_sinfo,Transaction

# Register your models here.

admin.site.register(Employee)
admin.site.register(Student_pinfo)
admin.site.register(Student_sinfo)
admin.site.register(Transaction)