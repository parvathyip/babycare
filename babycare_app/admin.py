from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Login)
admin.site.register(Panchayat)
# admin.site.register(Ward)
admin.site.register(Worker)
admin.site.register(Scheme)
admin.site.register(Mother)
admin.site.register(Child)
admin.site.register(Food)
admin.site.register(Tips)
admin.site.register(Healthcentre)
admin.site.register(Disease)
admin.site.register(VaccinationInfo)
# admin.site.register(VaccinationDate)