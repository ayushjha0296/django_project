from django.contrib import admin
from rango.models import restrict
from.models import UserProfile
#class restrictAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug':('name',)}
admin.site.register(restrict)
admin.site.register(UserProfile)
# Register your models here.
