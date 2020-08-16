from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Application_User)
admin.site.register(Manager_to_Mob)
admin.site.register(Task)
admin.site.register(Task_to_Mob)
admin.site.register(Submission)