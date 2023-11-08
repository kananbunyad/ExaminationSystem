from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'address', 'mobile', 'status', 'salary')
    search_fields = ['user__first_name', 'user__last_name', 'address', 'mobile']
    list_filter = ['status']

admin.site.register(Teacher, TeacherAdmin)