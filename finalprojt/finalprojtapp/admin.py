

# Register your models here.
from django.contrib import admin

from .models import District,SubBranches,contactdetails
admin.site.register(District)
admin.site.register(SubBranches)
admin.site.register(contactdetails)