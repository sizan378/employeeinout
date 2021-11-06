from django.contrib import admin, auth
from .models import *

admin.site.register(author)
# admin.site.register(LoginLogoutLog)
admin.site.register(Support)
admin.site.register(Outtime)


class EmployeeIPModel(admin.ModelAdmin):
    list_display = ["__str__","employeeName"]
    search_fields = ["__str__"]
    class Meta:
        Model=EmployeeIP
admin.site.register(EmployeeIP, EmployeeIPModel)


admin.site.register(Attend)
admin.site.register(InOutTime)
