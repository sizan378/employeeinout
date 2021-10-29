from django.contrib import admin, auth
from .models import *

admin.site.register(author)
# admin.site.register(LoginLogoutLog)
admin.site.register(Intime)
admin.site.register(Outtime)

admin.site.register(Attend)
