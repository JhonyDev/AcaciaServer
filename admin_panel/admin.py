from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(AdminCred)
admin.site.register(ReportedAccounts)
admin.site.register(PaidUsers)
admin.site.register(UnPaidUsers)
