from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'address', 'mobile')
    search_fields = ['user__first_name', 'user__last_name', 'address', 'mobile']

admin.site.register(Student, StudentAdmin)