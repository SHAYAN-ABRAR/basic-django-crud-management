from django.db import models
from employee.models import Employee 

class Salary(models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pay_date = models.DateField()

    def __str__(self):
        return f"{self.employee.emp_name} - {self.pay_date}"