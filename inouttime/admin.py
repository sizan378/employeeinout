from django.contrib import admin, auth
from .models import *

admin.site.register(author)
# admin.site.register(LoginLogoutLog)
admin.site.register(Support)
admin.site.register(Outtime)
admin.site.register(EmployeeIP)
admin.site.register(Attend)
admin.site.register(InOutTime)
