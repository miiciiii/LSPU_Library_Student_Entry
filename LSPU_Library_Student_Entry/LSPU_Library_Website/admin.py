from django.contrib import admin
from .models import Student, Table_Status, History
# Register your models here.

admin.site.register(Student)
admin.site.register(Table_Status)
admin.site.register(History)
