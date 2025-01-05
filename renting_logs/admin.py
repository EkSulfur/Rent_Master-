from django.contrib import admin

from .models import Tenant, Admin,LeaseRecord, House

admin.site.register(Tenant)
admin.site.register(Admin)
admin.site.register(LeaseRecord)
admin.site.register(House)
