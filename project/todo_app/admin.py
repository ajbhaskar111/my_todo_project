from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Role)
admin.site.register(UserProfile)
admin.site.register(ToDoList)
admin.site.register(Department)
admin.site.register(Master)
admin.site.register(TaskAssociation)
