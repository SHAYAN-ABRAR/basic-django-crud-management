from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'emp_dept', 'is_deleted') 
    list_filter = ('is_deleted',)
    search_fields = ('emp_name', 'emp_id')
    
admin.site.site_header = "EmployeeMS Dashboard"
admin.site.site_title = "Abrar's CMS"
admin.site.index_title = "Welcome to the Employee Management System"