from django.db import models
from ckeditor.fields import RichTextField

class Employee(models.Model):
    # Fixed: Removed max_length from IntegerField
    emp_id = models.IntegerField() 
    emp_name = models.CharField(max_length=50)
    emp_dept = models.CharField(max_length=50)
    
    # Add this for your Soft Delete function
    is_deleted = models.BooleanField(default=False)
    
    emp_notes = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.emp_name