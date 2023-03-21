from django.conf import settings
from django.db import models
from django.utils import timezone

class Departments(models.Model):
    department_id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=50)
    parent_id = models.SmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.department_id + "\t" + self.name
    
    def get_title(self):
        return '部署ID: {} 部署名: {}'.format(self.department_id, self.name)
    
    class Meta:
        db_table = 'm_departments'

class Employees(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    login_id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def update(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.last_name

    class Meta:
        db_table = 'm_employees'

class TimeMnagements(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    work_date = models.CharField(max_length=8)
    in_time = models.CharField(max_length=4, null=True, blank=True)
    out_time = models.CharField(max_length=4, null=True, blank=True)
    work_minutes = models.CharField(max_length=4, default='0')
    overtime_minutes = models.CharField(max_length=4, default='0')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_time_managements'





